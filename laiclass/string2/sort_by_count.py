'''
Created on Oct 2, 2017

@author: qiankunhuang
'''


def sort_by_count(A):
    dict = {}
    for i in A:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return sorted(A, key=lambda x: dict[x])


A = "aaabccd"
print(sort_by_count(A))
