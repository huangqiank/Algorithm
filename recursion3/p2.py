'''
Created on Feb 15, 2018

@author: qiankunhuang
'''
def find_str_permutation(A):
    index = 0
    n = len(A)
    res=[]
    help(n,index,res,A)
def help(n,index,res,A):
    if index == n:
        print res
        return
    for i in A:
        if i not in res:
            res.append(i)
            help(n,index+1,res,A)
            res.pop()    
A = ["a","b","c"]
find_str_permutation(A)
            
        
    
        
    
    
    
    
        
        
        
            