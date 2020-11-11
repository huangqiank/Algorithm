def first_occur(s):
    a = []
    b = {}
    for i in s:
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1
    for i in b.keys():
        if b[i] == 1:
            a.append(i)
    return a


def shift(A, k):
    a = A[:k]
    b = A[k:]
    c = b + a
gg
    return "".join(c)


def sort_by_count(a):
    d={}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] =1


