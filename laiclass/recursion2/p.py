'''
Created on Dec 8, 2017

@author: qiankunhuang
'''


def dfs_preorder(node):
    if node is None:
        return
    res = []
    help2(node, res)


def help2(node, res):
    if node is None:
        return res
    res.append(node.value)
    help2(node.left, res)
    help2(node.right, res)


def find_parathensis(n):
    left = 0
    right = 0
    res = []
    help4(left, right, res, n)


def help4(left, right, res, n):
    if left == n and right == n:
        print
        res
        return
    if left < n:
        res.append("(")
        help4(left + 1, right, res, n)
        res.pop()
    if right < left:
        res.append(")")
        help4(left, right + 1, res, n)
        res.pop()


def find_all_subset(input):
    res = []
    index = 0
    n = len(input)
    find_all_subset_help(input, res, index, n)


def find_all_subset_help(input, res, index, n):
    if n == index:
        print(res)
        return
    res.append(input[index])
    find_all_subset_help(input, res, index + 1, n)
    res.pop()
    find_all_subset_help(input, res, index + 1, n)


def str_permutation(a):
    index = 0
    n = len(a)
    res = []
    str_permutation_help(a, index, n, res)


def str_permutation_help(a, index, n, res):
    if index == n:
        if len(res) == 3:
            print(res)
        return
    for i in range(index, n):
        res.append(a[i])
        str_permutation_help(a, index + 1, n, res)
        res.pop()


def str_permutation_help2(a, index, n, res):
    if index == n:
        if len(res) == 3:
            print(res)
        return
    for i in range(index, n):
        a[i], a[index] = a[index], a[i]
        str_permutation_help2(a, index + 1, n, res)
        a[i], a[index] = a[index], a[i]


def permutation(input):
    l = 0
    r = 0
    n = len(input) / 2
    res = []
    find_permutation(l, r, n, res, input)


def find_permutation(l, r, n, res, input):
    if l == n and r == n:
        print(res)
        return
    if l < n:
        res.append("(")
        find_permutation(l + 1, r, n, res, input)
        res.pop()
    if l > r:
        res.append(")")
        find_permutation(l, r + 1, n, res, input)
        res.pop()
