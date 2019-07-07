'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def nearest_number(a,k):
    i = 0
    j = len(a)-1
    while i < j-1 :
        mid = (i + j)/2
        if a[mid] > k:
            j = mid
        if  a[mid] < k:
            i = mid
        if  a[mid] == k:
            return mid
    if abs(a[i]-k) < abs(a[j]-k):
        return i,a[i]
    else:
        return j,a[j]
a=[1,2,3,4,5,7,10,20]
print nearest_number(a,19)