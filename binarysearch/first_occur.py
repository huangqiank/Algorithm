'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def bfs_first_occur(a,k):
    i = 0
    j = len(a)-1
    while i < j-1:
        mid = (i + j)/2
        if a[mid] >= k:
            j = mid 
        if a[mid] < k:
            i = mid
    if a[i] == k:
        return i
    else:
        return j
a=[1,2,3,4,5,5,5]
print bfs_first_occur([1,2,3,4,5,5,5],5)
            
  
    