'''
Created on Sep 9, 2017

@author: qiankunhuang
'''

'''
先不断二分，再完向上合并
'''


def merge(a):
    if len(a) == 0 or len(a) == 1:
        return a
    mid = int(len(a) / 2)
    b = merge(a[:mid])
    c = merge(a[mid:])
    return merge_helper(b, c)


def merge_helper(b, c):
    d = []
    while len(b) != 0 and len(c) != 0:
        if b[0] < c[0]:
            d.append(b[0])
            del (b[0])
        else:
            d.append(c[0])
            del (c[0])
    if len(b) != 0:
        d += b
    if len(c) != 0:
        d += c
    return d


a = [0, 10, 2, 3, 8, 5]
print(merge(a))
a = [1, 2, 3, 4]
print(a[1:3])
