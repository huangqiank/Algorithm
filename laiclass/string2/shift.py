'''
Created on Oct 2, 2017

@author: qiankunhuang
'''
def shift(A,k):
    a=A[:k]
    b=A[k:]
    c = b+a
    return "".join(c)
print(shift("abcd",1))

def shift2(A,k):
    B=list(A)
    B=B[::-1]
    A = B[:k]
    C = B[k:]
    A = A[::-1]
    C= C[::-1]
    D= A+C
    return "".join(D)
print (shift2("abcd",1))

