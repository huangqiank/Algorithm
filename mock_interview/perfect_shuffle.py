'''
Created on Oct 21, 2017

@author: qiankunhuang
'''
def permutation(lst):
    n=len(lst)
    for i in xrange(n-1,-1,-1):
        rand=random.randint(0,i)
        lst[rand]