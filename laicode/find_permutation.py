'''
Created on Jan 28, 2018

@author: qiankunhuang
'''
def find_permutation(a):
    index= 0
    n =len(a)
    res=[]
    help(a,n,index,res)
def help(a,n,index,res):
    if index ==n:
        print res
        return
    for i in a:
        if i not in res:
            res.append(i)
            help(a,n,index+1,res)
            res.pop()
def find_permutation2(a):
    index = 0 
    help2(a,index)
def help2(a,index):
    if index == len(a):
        print a
        return
        print 
    for i in range(index,len(a)):
        a[index],a[i]=a[i],a[index]
        help2(a,index+1)
        a[i],a[index]=a[index],a[i]
        
def find_permutation3(a):
    if not a:
        return a
    index= 0vt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    \
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    n =len(a)
    res=[]
    path=[]
    help3(a,n,index,res,path)
    return path
def help3(a,n,index,res,path):
    if index ==n:
        path.append(res)
        return
    for i in a:
        if i not in res:
            res.append(i)
            help(a,n,index+1,res)
            res.pop()
find_permutation3([1,2,3])
    
            