'''
Created on Oct 2, 2017

@author: qiankunhuang
'''


def reverse(a):
    i = 0
    n =len(a)
    res= []
    if not a or n ==0:
        return a
    while i < n:
        c=[]
        while i < n and a[i] != " " :
            c.append(a[i])
            i+=1
        c.reverse()
        res.extend(c)
        res.append(" ")
        i+=1
    return "".join(res)
S = "abc de fg"
print(reverse(S))


