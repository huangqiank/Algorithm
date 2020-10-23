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
###       (1.04(杭州504万买房贷款226首付338) +  7.28 (润府贷款) ) * 12   +  100000 (小孩读书,生活费) +  100000(生活费) + 200000(邢路工资)   = 1527528
###   收入:
###       1000000(黄平)  + 20000000* 2.6% (股票收入) =  1527528


def quick(list):
    p = 0
    q = len(list) - 1
    help(list, p, q)
    return list


def help(a, p, q):
    if p < q:
        t = partiton(a, p, q)
        help(a, p, t - 1)
        help(a, t + 1, q)


def partiton(a, p, q):
    left = p - 1
    i = p
    while i < q:
        if a[i] < a[q]:
            left += 1
            a[left], a[i] = a[i], a[left]
            i += 1
        else:
            i += 1
    left += 1
    a[q], a[left] = a[left], a[q]
    return left


def merge(node_list):
    if len(node_list) == 0 or len(node_list) == 1:
        return node_list
    mid = len(node_list) / 2
    left = merge(node_list[:mid])
    right = merge(node_list[mid:])
    return merge_help(left, right)


def merge_help(left, right):
    res = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            res.append(left[0])
            del left[0]
        else:
            res.append(right[0])
            del right[0]
    if len(left) != 0:
        res.extend(left)
    else:
        res.extend(right)
    return res


def quick(list):
    p = 0
    q = len(list) - 1
    quick_sort(list, p, q)
    return list


def quick_sort(list, p, q):
    if p < q:
        d = partition(list, p, q)
        quick_sort(list, p, d - 1)
        quick_sort(list, d + 1, q)
    return list



## 开支:
##(10312(杭州500万买房贷款) +  72807 (润府贷款) ) * 12  +  100000 (小孩读书,生活费) +  100000(生活费) + 240000(邢路工资)   = 1527528
##收入:
##1000000(黄平)  + 20000000* 2.6% (股票收入) =  1527528
