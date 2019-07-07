'''
Created on Oct 8, 2017

@author: qiankunhuang
'''
def minimum_window_string(A,B):
    c= dict()
    for i in A:
        if i not in c:
            c[i] = 1
        else:
            c[i] += 1
    e=dict()
    n = len(B)
    j=0
    while j < n:
        if B[j] == A[0]:
            while j < n 
                j+=1