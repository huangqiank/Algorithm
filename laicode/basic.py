'''
Created on Jan 28, 2018

@author: qiankunhuang
'''
def g():
    print x
    x=1
x=3
# g()
## local two types of defination  1, outside 2,inside
def f(*arg,**kargs):
    print arg,kargs
f(1,2,3,lastname='Chen',firstname='Shan')
# *arg xingcan , **kargs mingcan
zip([1,2,3],[3,4,5,6])
for index,element in enumerate([1,2,3]):
    print (index,element)

