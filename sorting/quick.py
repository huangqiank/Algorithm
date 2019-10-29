'''
Created on Sep 9, 2017

@author: qiankunhuang
'''


def quick(input):
    q = len(input) - 1
    p = 0
    return quick_sort(input, p, q)


def quick_sort(a, p, q):
    if p < q:
        d = partion(a, p, q)
        quick_sort(a, p, d - 1)
        quick_sort(a, d + 1, q)
    return a


def partion(a, p, q):
    j = p - 1
    for i in range(p, q, 1):
        if a[i] < a[q]:
            j += 1
            a[j], a[i] = a[i], a[j]
    j += 1
    a[q], a[j] = a[j], a[q]
    return j


a = [0, 10, 2, 3, 8, 5, -1]
print(quick(a))
print(quick_sort(a, 0, 6))
