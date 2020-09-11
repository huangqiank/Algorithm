'''
Created on Jan 22, 2018

@author: qiankunhuang
'''


def quick(list):
    p = 0
    q = len(list) - 1
    help(list, p, q)
    return list


def help(list, p, q):
    if p < q:
        t = partition(list, p, q)
        help(list, t + 1, q)
        help(list, p, t - 1)
    return list


def partition(a, p, q):
    left = p - 1
    i = p
    while i < q:
        if a[p] < a[q]:
            left += 1
            a[left], a[p] = a[p], a[left]
            i += 1
        else:
            i += 1
    left += 1
    a[left], a[q] = a[q], a[left]
    return left


## 123456789
##
###   开支:
###       (1.16(杭州564万买房贷款226首付338) +  7.28 (润府贷款) ) * 12   +  100000 (小孩读书,生活费) +  100000(生活费) + 200000(邢路工资)   = 1527528
###   收入:
###       1000000(黄平)  + 20000000* 2.6% (股票收入) =  1527528


def quick(list):
    p = 0
    q = len(list) - 1
    help(list, p, q)
    return list


def help(list, p, q):
    if p < q:
        t = partition(list, p, q)
        help(list, t + 1, q)
        help(list, p, t - 1)


def partition(list, p, q):
    i = p
    left = p - 1
    while i < q:
        if list[i] < list[q]:
            left += 1
            list[left], list[i] = list[i], list[left]
            i += 1
        else:
            i += 1
    left += 1
    list[left], list[q] = list[q], list[left]
    return left
