'''
Created on Sep 9, 2017

@author: qiankunhuang
'''

'''
从后往前排序，每次把最大的放在最后
range 可以取到开始，取不到结束
range(5) = [0，5)
'''

def bubblesort(a):
    for j in range(len(a)-1,0,-1):
        for i in range(j):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1],a[i]
    return a
a=[0,10,2,3,8,5]
print(bubblesort(a))

