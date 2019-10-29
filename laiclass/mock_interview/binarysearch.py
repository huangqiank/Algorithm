'''
Created on Oct 21, 2017

@author: qiankunhuang
'''
def binarysearch(A,k):
    right = len(A)-1
    left = 0
    while left+1 < right:
        mid = (left+right)/2
        if A[mid] < k:
            left = mid
        if A[mid] > k:
            right = mid-1
        if A[mid] == k:
            return mid
    if A[right] < k:
        return right+1
    else:
        if A[left]>k:
            return left
        else:
            return left+1
        
    