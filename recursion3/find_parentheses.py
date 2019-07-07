'''
Created on Sep 26, 2017

@author: qiankunhuang
'''
def permutation(input):
    n = len(input)/2
    l = 0
    r = 0
    res = []
    find_permutation(l,r,n,res)
    
def find_permutation(l,r,n, res):
    if l == n and r == n:
        print res
        return
    if l < n:
        res.append("(")
        find_permutation(l+1,r,n, res)
        res.pop()
    if r < l:
        res.append(")")
        find_permutation(l,r+1,n,res)
        res.pop()
        
input = ["(","(",")",")","(",")"]     
permutation(input)
        
        
        
    