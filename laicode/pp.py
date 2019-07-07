'''
Created on Feb 7, 2018

@author: qiankunhuang
'''
def f(n,list):
    res= 0 
    for i in xrange(n):
        for j in xrange(n-i):
            new_list = list[j:i+j]
            if len(new_list)>0:
                total=sum(new_list)
                small =min(new_list)
                res=max(res,small*total)
    return res
print f(10,[81,87,47,59,81,18,25,40,56,0])

a= [1,2,3]
print a[0:2]
            