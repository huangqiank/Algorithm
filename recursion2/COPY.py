'''
Created on Feb 5, 2018

@author: qiankunhuang
'''
#shallow copy：copy reference
def remove(l1,l2):
    for e in l1:
        if e in l2:
            l1.remove(e)
#deep copy:copy all
def remove2(l1,l2):
    for e in l1[:]:
        if e in l2:
            l1.remove(e)
a=[1,2,3,4]
res=[]
res1=[]
res.append(a)
res1.append(a[:])
a.pop(0)

print (res,res1)