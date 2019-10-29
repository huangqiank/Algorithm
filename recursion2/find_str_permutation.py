'''
Created on Sep 26, 2017

@author: qiankunhuang
'''


def print_permutation(A):
    index = 0
    res = []
    n = len(A)
    permutation2(A, index)


def permutation(index, A, res, n):
    if index == n:
        print(res)
        return
    for j in A:
        if j not in res:
            res.append(j)
            permutation(index + 1, A, res, n)
            res.pop()


def permutation2(input, index):
    if index == len(input):
        print(input)
        return
    for i in range(index, len(input)):
        input[index], input[i] = input[i], input[index]
        permutation2(input, index + 1)
        input[index], input[i] = input[i], input[index]


A = ["a", "b", "c"]

print_permutation(A)
permutation(0,A,[],3)