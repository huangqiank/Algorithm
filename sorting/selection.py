'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def selection(a):
    for i in range(len(a)):
        min=i
        for j in range(i,len(a),1):
            if a[min] > a[j]:
                min = j
        a[min],a[i] = a[i],a[min]
    return a
a=[0,10,2,3,8,5]
print (selection(a))



