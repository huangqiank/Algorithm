'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
def binarysearch(a,k):
    i = 0
    j = len(a)-1 
    while i <= j:
        mid = (i+j)/2
        if a[mid] == k:
            return mid
        if a[mid] > k:
            j = mid - 1
        if a[mid] < k:
            i = mid + 1
    return False

print binarysearch([1,2,3,5],4)


def first_occur(array,target):
    right = len(array)-1
    left = 0
    while left+1 < right:
        mid = (left+right)/2
        if array[mid] >= target:
            right = mid
        else:
            left = mid
    if array[left] == target:
        return left
    if array [right] == target:
        return right
arr = [1,2,3,3,5,7,9]
first_occur(arr,3)
