'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
import math


def binarySearch(a, b):
    n = len(a)
    left = 0
    right = n - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if a[mid] > b:
            right = mid
        if a[mid] == b:
            return mid
        if a[mid] < b:
            left = mid
    if a[left] == b:
        return left
    if a[right] == b:
        return right
    return False


print(binarySearch([1, 2, 3, 4, 5, 6], 6))



def first_occur(array, target):
    right = len(array) - 1
    left = 0
    while left + 1 < right:
        mid = int((left + right) / 2)
        if array[mid] >= target:
            right = mid
        else:
            left = mid
    if array[left] == target:
        return left
    if array[right] == target:
        return right


arr = [1, 2, 3, 3, 5, 7, 9]
print(first_occur(arr, 3))
