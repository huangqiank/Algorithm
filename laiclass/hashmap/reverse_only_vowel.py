'''
Created on Jan 20, 2018

@author: qiankunhuang
'''


def remove(a):
    if not a or len(a) == 0:
        return input
    v = ['a', 'e', 'i', 'o', 'u']
    n = len(a)
    i = 0
    res = []
    index = []
    while i < n:
        if a[i] in v:
            index.append(i)
            res.append(a[i])
            i += 1
        else:
            res.append(a[i])
            i += 1
    if len(index) == 0:
        return ''.join(res)
    old = index[:int(len(index) / 2)]
    new = index[len(index) - 1:int(len(index) / 2) - 1:-1]
    for i in range(len(old)):
        res[old[i]], res[new[i]] = res[new[i]], res[old[i]]
    return ''.join(res)


print(remove('awriou'))

## a w r i o u
## u o i r w a
