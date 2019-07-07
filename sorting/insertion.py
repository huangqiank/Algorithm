'''
Created on Sep 9, 2017

@author: qiankunhuang
'''

def insertion2(A):
    for i in xrange(0,len(A),1):
        for j in xrange(i,1,-1):
            if A[j]<A[j-1]:
                A[j], A[j-1] = A[j-1],A[j]
            else:
                break
    return A   
a=[0,10,20,3,8,5,7,7]
print insertion2(a)
     

            