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
    return "".join(c)


def sort_by_count(a):
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return sorted(d, key=lambda x: d[x])


def reverse(a):
    i = 0
    if not a or len(a) == 0:
        return
    c = []
    res = []
    while i < len(a):
        if a[i] != " ":
            c.append(a[i])
        else:
            c.reverse()
            res.extend(c)
            res.append(" ")
            c = []
        i += 1
    res.extend(c)
    return "".join(res)


def remove_space(a):
    if not a or len(a) == 0:
        return a
    i = 0
    n = len(a)
    res = []
    while i < n:
        if a[i] == " ":
            j = i
            res.append(a[i])
            while j < n and a[j] == " ":
                j += 1
            i = j
        else:
            res.append(a[i])
            i += 1
    if res[0] == " ":
        res.pop(0)
    if res[-1] == " ":
        res.pop()
    return "".join(res)


def remove_adjacent(a):
    if a is None or len(a) == 0:
        return a
    i = 0
    n = len(a)
    res = []
    while i < n:
        if len(res) == 0 or res[-1] != a[i]:
            res.append(a[i])
            i += 1
        else:
            i += 1
    return "".join(res)


def remove_adjacent2(a):
    i = 0
    n = len(a)
    res = []
    if not a or len(a) == 0:
        return a
    while i < n:
        if len(res) < 2 or a[i] != res[-1] or a[i] != res[-2]:
            res.append(a[i])
            i += 1
        else:
            i += 1
    return "".join(res)


def remove_adjacent3(a):
    res = []
    i = 0
    n = len(a)
    if not a or len(a) == 0:
        return a
    while i < n:
        if len(res) != 0 and res[-1] == a[i]:
            k = a[i]
            while i < n and a[i] == k:
                i += 1
            res.pop()
        else:
            res.append(a[i])
            i += 1
    return res


def longest_no_duplicated(s):
    if s is None or len(s) == 0:
        return
    cur_length = 1
    max_length = 1
    dict_index = {}
    dict_index[s[0]] = 1
    for i in range(1, len(s), 1):
        if s[i] not in dict_index:
            dict_index[s[i]] = i
            cur_length += 1
        else:
            index = dict_index[s[i]]
            if index + cur_length >= i:
                max_length = max(max_length, cur_length)
                cur_length = i - index
                dict_index[s[i]] = i
            else:
                dict_index[s[i]] = i
                cur_length += 1
    max_length = max(max_length, cur_length)
    return max_length
