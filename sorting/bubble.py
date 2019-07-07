'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def bubblesort(a):
    for j in xrange(len(a)-1,0,-1):
        for i in xrange(j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1],a[i]
    return a
a=[0,10,2,3,8,5]
print bubblesort(a)

