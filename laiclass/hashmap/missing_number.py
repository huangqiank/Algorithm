'''
Created on Sep 30, 2017

@author: qiankunhuang
'''
def missing_number1(A):
    B=set(A)
    for i in xrange(0,101,1):
        if i not in B:
            return i
def missing_number2(A):
    sum = 0
    for i in A:
        sum += A[i]
    return 5050 - sum

            