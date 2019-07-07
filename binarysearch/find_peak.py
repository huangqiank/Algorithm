'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def bfs_peak(a):
    i=0
    j=len(a)-1
    while i < j-1 :
        mid = (i+j)/2
        if a[mid] > a[mid-1] and a[mid] > a[mid+1] :
            return mid
        if  a[mid] < a[mid-1]: 
            j = mid
        if  a[mid] > a[mid-1] and a[mid] < a[mid+1]:
            i = mid
    if a[i] > a[j]:
        return i
    else:
        return j
    
a = [1,3,1,4,5,6,7,8,9,10,2]
print bfs_peak(a)
        