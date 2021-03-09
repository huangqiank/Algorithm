'''
Created on Dec 13, 2017

@author: qiankunhuang
'''


def longest(input):
    if not input or len(input) == 0:
        return 0
    n = len(input)
    Max = 0
    for i in range(0, n, 1):
        a = set()
        for j in range(i, n, 1):
            if input[j] not in a:
                a.add(input[j])
            else:
                Max = max(Max, len(a))
                break
    return Max


def length_last_word(word):
    n = len(word) - 1
    last = 0
    while n > 0 and word[n] == " ":
        n -= 1
    while n > 0 and word[n] != " ":
        n -= 1
        last += 1
    return last


def longest_common_prefix(str_list):
    if not str_list:
        return ""
    shortest = min(str_list, key=len)
    for i, char in enumerate(shortest):
        for chars in str_list:
            if chars[i] != char:
                return shortest[:i]
    return shortest


def find_nearest_entry(arr):
    word_ind = {}
    dist = len(arr)
    for i in range(len(arr)):
        if arr[i] in word_ind:
            dist = min(dist, i - word_ind[arr[i]])
        word_ind[arr[i]] = i
    return dist


def reverse_word(input):
    word = []
    res = []
    i = 0
    n = len(input)
    while i < n:
        if " " != input[i]:
            word.append(input[i])
        else:
            res.append(word)
            word = []
        i += 1
    res.append(word)
    res.reverse()
    return " ".join([''.join(i) for i in res])


def remove_space(a):
    if a is None or len(a) == 0:
        return a
    lst = []
    for i in range(len(a)):
        if a[i] == " " and (i == 0 or a[i - 1] == " "):
            continue
        lst.append(a[i])
    if lst[-1] == " ":
        return "".join(lst)


def sub_string(a, b):
    if len(a) <= len(b):
        min_str = a
        max_str = b
    else:
        min_str = b
        max_str = a
    for j in range(len(max_str)):
        if max_str[j] == min_str[0]:
            for i in range(len(min_str)):
                if max_str[j + i] != min_str[i]:
                    break
                if i == len(min_str) - 1:
                    return True
    return False


print(sub_string("abcde", "dabcdfef"))

print(sub_string("abc", "dabc"))


def find_nearest(arr):
    word_ind = {}
    dist = 0
    for i in range(len(arr)):
        if arr[i] in word_ind:
            dist = max(dist, i - word_ind[arr[i]])
        word_ind[arr[i]] = i
    return dist


def longest_common_prefix(str_list):
    if not str_list:
        return
    res = []
    shortest = min(str_list, key=len)
    for i, ch in enumerate(shortest):
        for other in str_list:
            if other[i] == shortest[i]:
                res.append(shortest[i])
            else:
                return res


def find_nearest_entry(arr):
    word_dict = {}
    dist = len(arr)
    for i in range(len(arr)):
        if arr[i] not in word_dict:
            word_dict[arr[i]] = i
        else:
            dist = min(i - word_dict[arr[i]], dist)
    return dist
