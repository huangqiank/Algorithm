'''
Created on Sep 9, 2017

@author: qiankunhuang
'''


def firstOccur(a, b):
    left = 0
    right = len(a) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if a[mid] >= b:
            right = mid
        if a[mid] < b:
            left = mid
    if a[left] == b:
        return left
    if a[right] == b:
        return right
    return False



a1 = [1,2,3,3,3]
a2 = [3,3,3,4,5]
print(firstOccur(a1,3))
print(firstOccur(a2,3))


def firstOccur2(a,b):
    left = 0
    right = len(a)-1
    while left < right:
        mid =int((left+right)/2)
        if a[mid] < b :
            left = mid + 1
        if a[mid] > b :
            right = mid-1
        if a[mid] == b:
            right = mid
    print("left :" + str(left))
    print("right :" + str(right))
    if a[left] == b :
        return left
    if a[right] ==b:
        return right
    return False


a1 = [1,2,3,3,3]
a2 = [3,3,3,4,5]
print(firstOccur2(a1,3))
print(firstOccur2(a2,3))