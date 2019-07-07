'''
Created on Oct 2, 2017

@author: qiankunhuang
'''

def fist_occur2(A):
    if A is None or len(A)== 0 :
        return 
    B={}
    c=[]
    for i in A:
        if i not in B:
            B[i] = 1
        else:
            B[i] += 1
    for i in A:
        if B[i] == 1:
            c.append(i)
    return c
print fist_occur2("abfcdef")
                   
            