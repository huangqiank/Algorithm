#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
import pickle

import jieba
import keras.backend as K
import numpy as np
import pandas as pd
import tensorflow as tf
from algorithm.text_normalize import TextNorm
from keras.losses import categorical_crossentropy
from keras.metrics import categorical_accuracy
from keras.models import load_model


def categorical_crossentropy_modified(y_true, y_pred):
    mark = y_true[:, 0]
    indices = tf.where(K.not_equal(mark, -1))
    y_true = tf.gather_nd(y_true, indices)
    y_pred = tf.gather_nd(y_pred, indices)

    normalizer = K.cast(K.shape(indices)[0], K.floatx())
    normalizer = K.maximum(1.0, normalizer)
    return K.sum(categorical_crossentropy(y_true, y_pred)) / normalizer


def categorical_accuracy_modified(y_true, y_pred):
    mark = y_true[:, 0]
    indices = tf.where(K.not_equal(mark, -1))
    print(indices.shape)
    y_true = tf.gather_nd(y_true, indices)
    y_pred = tf.gather_nd(y_pred, indices)
    return categorical_accuracy(y_true, y_pred)


class Taxonomy:
    def __init__(self):
        # path dir
        dir = os.path.abspath(os.path.dirname(__file__))
        self.model_path = os.path.join(dir, "data/taxonomy.h5")

        # load pkl
        self.white_word = (pickle.load(open(os.path.join(dir, "data/white_word.pkl"), "rb")))
        self.qiangda_white_word = (pickle.load(open(os.path.join(dir, "data/qiangda_white_word.pkl"), "rb")))
        ##self.change_word = (pickle.load(open(os.path.join(dir, "data/change_word.pkl"), "rb")))
        ##self.statistic = (pickle.load(open(os.path.join(dir, "data/lv2_statistic.pkl"), "rb")))
        ##self.statistic_word = set(self.statistic.keys())
        self.lv2_ids = list(pickle.load(open(os.path.join(dir, "data/lv2_id_name_map.pkl"), "rb")).keys())
        self.parent = pickle.load(open(os.path.join(dir, "data/child_parent_map.pkl"), "rb"))
        self.id_name_map = pickle.load(open(os.path.join(dir, "data/id_name_map.pkl"), "rb"))
        self.right_sex_prods = pickle.load(open(os.path.join(dir, "data/right_sex_prod.pkl"), "rb"))
        self.change_sex_prods = pickle.load(open(os.path.join(dir, "data/change_sex_prods.pkl"), "rb"))
        print('INFO', 'Taxonomy init, lv2 length:', len(self.lv2_ids))
        print('INFO', 'Taxonomy init, parent length:', len(self.parent))
        print('INFO', 'Taxonomy init, lv1+lv2 length:', len(self.id_name_map))

        ### load dict

        ##self.vocab = self.load_word2vec_vocab(self.dic_path)
        self.vocab = pickle.load(open(os.path.join(dir, "data/dic.pkl"), "rb"))
        self.cnt = set()

        ### load model
        print("Taxonomy init, load model. ", self.model_path)
        self.model = load_model(self.model_path,
                                custom_objects={'categorical_accuracy_modified': categorical_accuracy_modified,
                                                'categorical_crossentropy_modified': categorical_crossentropy_modified})
        self.male = "男"
        self.female = "女"
        self.middle = "中性"

    def load_word2vec_vocab(self, file):
        vocabulary_vector = dict(pd.read_csv(file))
        vocabulary = {}
        index = 0
        # 此时需要将字典中的词向量np.array型数据还原为原始类型，方便以后使用
        for key, index in vocabulary_vector.items():
            vocabulary[key] = index
        return vocabulary

    def normal_predict(self, query, threshold, n):
        fenci_res = " ".join(jieba.cut(query))
        print(fenci_res)
        text_vectors = self.extract_feature([fenci_res])
        result = self.predict_with_score(text_vectors, threshold, n)
        # K.clear_session()
        return result

    def predict(self, query, threshold, n, user_sex=None):
        query = TextNorm().normalization(query)
        ##if query in self.white_word.keys():
        ##    return self.white_word[query]
        ##if query in self.qiangda_white_word.keys():
        ##    return self.qiangda_white_word[query]
        ##if query in self.change_word.keys():
        ##    return self.change_word[query]
        ##if query in self.statistic_word:
        ##    return self.statistic[query]
        sex = self.check_sex_help(query, user_sex)
        res = self.check_prod_sex(query, sex)
        return res

    def check_sex_help(self, query, user_sex):
        if self.male in query or self.female in query:
            return self.middle
        if user_sex == self.male:
            return self.male
        if user_sex == self.female:
            return self.female
        return self.middle

    def check_prod_sex(self, query, sex):
        ## 考虑加入分词的结果匹配
        if sex == self.middle:
            if query in self.change_sex_prods.keys():
                return self.change_sex_prods[query]
        ##fenci_list = list(jieba.cut(query))
        new_query = sex + query
        if query in self.right_sex_prods:
            return self.normal_predict(new_query, 0.1, 3)
        if new_query in self.change_sex_prods.keys():
            return self.change_sex_prods[new_query]
        return self.normal_predict(query, 0.1, 3)

    def extract_feature(self, querys):
        ##训练数据已经分好词了
        ids = len(querys)
        query_vectors = {}
        for index, query in enumerate(querys):
            query_vectors[index] = self.__vectorize(query)
        return np.array([query_vectors.get(id, np.zeros(20)) for id in range(ids)])

    def __vectorize(self, query):
        length = 20
        query_vector = np.zeros(20)
        idx = 0
        words = query.split()
        for word in words:
            if word in self.vocab and idx < length:
                query_vector[idx] = self.vocab[word]
                idx += 1
        return query_vector

    def __probs_to_classes_with_score(self, predict_probs, threshold, n):
        res = {}
        prob_lv2 = predict_probs[0]
        lv2_result = prob_lv2.argsort(axis=-1)
        for i in range(1, n + 1):
            if prob_lv2[lv2_result[-i]] > threshold:
                id_key = "top_" + str(i) + "_id"
                score_key = "top_" + str(i) + "_score"
                name_key = "top_" + str(i) + "_name"
                res[id_key] = self.lv2_ids[lv2_result[-i]]
                res[name_key] = self.id_name_map[res[id_key]]
                res[score_key] = str(prob_lv2[lv2_result[-i]])
        return res

    def predict_with_score(self, text_vectors, threshold, n):
        predict_probs = self.model.predict([text_vectors[:, :20]])
        return self.__probs_to_classes_with_score(predict_probs, threshold, n)


def test():
    a = Taxonomy()
    words = ["金立手机", "男靴", "超轻羽绒服男", "皮衣", "金箍棒",
             "秋衣半高领女外穿", "手机oppo r17", "荣耀8总成屏/荣耀8总成",
             "万圣节儿童服装/万圣节服装男童/万圣节服装", "	手机oppo r17手机",
             "苹果x", "oppo手机A11", "手表带", "新生儿用品", "睡衣男"]
    for word in words:
        print(word)
        print(a.predict(word, 0.000000000000001, 3, "0"))
    print("用品")
    print(a.predict("用品", 0.000000000000001, 3, "0"))

def check_query():
    path = "/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/prod_res.csv"
    path1 = "/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/male_res.csv"
    path2 = "/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/female_res.csv"
    cat_path = "/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/二级类目树.csv"
    male_query_predict = {}
    female_query_predict = {}
    heads = ["query", "top_1_parent_name", "top_1_name", "top_1_id", "top_1_score"]
    for head in heads:
        male_query_predict[head] = []
        female_query_predict[head] = []
    id_name = {}
    lv1_lv2_id = {}
    model = Taxonomy()
    with open(cat_path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            new_cat_id_1_id, new_cat_id_2_id, new_cat_id_1_name, new_cat_id_2_name = row
            id_name[new_cat_id_1_id] = new_cat_id_1_name
            id_name[new_cat_id_2_id] = new_cat_id_2_name
            lv1_lv2_id[new_cat_id_2_id] = new_cat_id_1_id
    with open(path) as csvfile:  #
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            query = row[0]
            male_res = model.predict(query, 0.1, 3, "男")
            female_res = model.predict(query, 0.1, 3, "女")

            top_1_id = male_res.get('top_1_id', "")
            if top_1_id == "":
                top_1_parent_name = ""
            else:
                top_1_parent_name = id_name[lv1_lv2_id[top_1_id]]
            male_query_predict['query'].append(query)
            male_query_predict['top_1_name'].append(male_res.get('top_1_name', ""))
            male_query_predict['top_1_id'].append(top_1_id)
            male_query_predict['top_1_parent_name'].append(top_1_parent_name)
            male_query_predict["top_1_score"].append(male_res.get('top_1_score', ""))

            top_1_id = female_res.get('top_1_id', "")
            if top_1_id == "":
                top_1_parent_name = ""
            else:
                top_1_parent_name = id_name[lv1_lv2_id[top_1_id]]
            female_query_predict['query'].append(query)
            female_query_predict['top_1_parent_name'].append(top_1_parent_name)
            female_query_predict['top_1_name'].append(female_res.get('top_1_name', ""))
            female_query_predict['top_1_id'].append(top_1_id)
            female_query_predict["top_1_score"].append(female_res.get('top_1_score', ""))
    pd.DataFrame(male_query_predict).to_csv(path1)
    pd.DataFrame(female_query_predict).to_csv(path2)


def creat_sex_pkl():
    path = "/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/change2.csv"
    doc_dict = {}
    with open(path) as csvfile:  #
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            if len(row) != 7:
                print(row)
            query, top_1_id, top_1_name, top_1_score, top_2_id, top_2_name, top_2_score = row

            predict_res = {}
            predict_res["top_1_id"] = top_1_id
            predict_res["top_1_name"] = top_1_name
            predict_res["top_1_score"] = str(top_1_score)
            predict_res["top_2_id"] = top_2_id
            predict_res["top_2_name"] = top_2_name
            predict_res["top_2_score"] = str(top_2_score)
            doc_dict[query] = predict_res
    pickle.dump(doc_dict,
                open("/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/change_sex_prods.pkl", "wb"))
    right_res = set()
    path = "/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/right.csv"
    with open(path) as csvfile:  #
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            query, res = row
            right_res.add(query)
    pickle.dump(right_res,
                open("/Users/xinglu/PycharmProjects/nlp_query_classifier/algorithm/data/right_sex_prod.pkl", "wb"))
