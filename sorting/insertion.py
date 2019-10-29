'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
'''
从前往后排序，每次把最小的放在最前面
range 可以取到开始，取不到结束
range(5) = [0，5)
保证前3个有序，再保证前5个有序，直到所有都是有序的
'''

def insertion2(A):
    for i in range(0,len(A),1):
        for j in range(i,1,-1):
            if A[j]<A[j-1]:
                A[j], A[j-1] = A[j-1],A[j]
            else:
                break
    return A   
a=[0,10,20,3,8,5,7,7]
print(insertion2(a))
     

            