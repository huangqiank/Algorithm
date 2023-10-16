##1268. 搜索推荐系统
# 给你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。
# 请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。
# 请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。
# 示例 1：
# 输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# 输出：[
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
class Trie():
    def __init__(self):
        self.children = {}
        self.pro = []

    def add(self, word):
        s = self
        for i in word:
            if i not in s.children:
                s.children[i] = Trie()
            s = s.children[i]
            s.pro.append(word)
            s.pro.sort()
            if len(s.pro) > 3:
                s.pro.pop()

    def search(self, word):
        s = self
        res = []
        for i in word:
            if i in s.children:
                s = s.children[i]
                res.append(s.pro)
            else:
                res.append([])
                s = Trie()
        return res


class Solution:
    def suggestedProducts(self, products, searchWord):
        t = Trie()
        for pro in products:
            t.add(pro)
        return t.search(searchWord)


a = [2, 1, 3]
a.sort()
print(a)
