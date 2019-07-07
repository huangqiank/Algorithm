'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def bfs_near_num(a,k):
    row = len(a)
    col = len(a[0])
    i = 0
    j = row*col-1
    while i <= j:
        mid = (i+j)/2
        c =  mid/col 
        b = mid%col 
        if a[c][b] == k:
            return c,b
        if a[c][b] > k:
            j = mid-1
        if a[c][b] < k:
            i = mid + 1
    return False 

def matrix(a,k):
    l=0
    row=len(a)
    col=len(a[0])
    r=col*row-1
    while l + 1 < r:
        mid=(l+r)/2
        if a[mid/col][mid%col] == k:
            return mid/col,mid%col
        if a[mid/col][mid%col] > k:
            r = mid
        if a[mid/col][mid%col] < k:
            l = mid 
    if a[l/col][l%col]==k:
        return l/col,l%col
    if a[r/col][r%col]==k:
        return r/col,r%col
    return False
d=[[1,2],[3,4]]
print bfs_near_num(d,3)   
            
      