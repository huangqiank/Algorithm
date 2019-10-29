'''
Created on Feb 18, 2018

@author: qiankunhuang
'''
def sum_k(A,k):
    n = len(A)
    index = 0
    res=[]
    help(A,index,k,res)

def help(A,index,k,res):
    if index == len(A):
        print res
        return
    for i in xrange(0,k/A[index]+1,1):
        res.append(i)
        help(A,index+1,k-A[index]*i)
        res.pop()
        
        
        