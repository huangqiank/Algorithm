'''
Created on Jan 25, 2018

@author: qiankunhuang
'''
def remove(s):
    if not s or len(s) == 0:
        return s
    lst = list(s)
    i,j=2,2
    while j<len(lst):
        if lst[j]!=lst[i-2]:
            lst[i] = lst[j]
            i+=1
        j+=1
    return lst[:-1]
    