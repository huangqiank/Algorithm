'''
Created on Jan 20, 2018

@author: qiankunhuang
'''


def k_closet(array, target, k):
    t = find(array, target)
    i = t
    j = t + 1
    res = []
    while k > 0:
        if i < 0:
            res.extend(array[j:j + k])
            return res
        if j > len(array) - 1:
            while k > 0:
                res.append(array[i])
                i -= 1
                k -= 1
            return res
        if abs(array[i] - target) <= abs(array[j] - target):
            res.append(array[i])
            i -= 1
            k -= 1
        if abs(array[i] - target) > abs(array[j] - target):
            res.append(array[j])
            j += 1
            k -= 1
    return res


def k_closet2(list, k, t):
    res = []
    left = 0
    right = len(list) - 1
    find = 0
    while left + 1 < right:
        mid = int((left + right) / 2)
        if list[mid] == k:
            left = mid
            break
        if list[mid] < k:
            left = mid
        if list[mid] > k:
            right = mid
    if abs(list[left] - k) <= abs(list[right] - k):
        find = left
    else:
        find = right
    left = find - 1
    right = find + 1
    res.append(list[find])
    while t - 1 > 0:
        if left < 0:
            if right > len(list) - 1:
                return res
            res.append(list[right])
            right += 1
            t -= 1
        else:
            if right > len(list) - 1:
                res.append(list[left])
                left -= 1
                t -= 1
            else:
                if abs(list[left] - k) <= abs(list[right] - k):
                    res.append(list[left])
                    left -= 1
                    t -= 1
                else:
                    res.append(list[right])
                    right += 1
                    t -= 1
    return res


print(k_closet2([1, 2, 3, 4, 5, 6], 2, 4))


def find(array, target):
    left = 0
    right = len(array) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if array[mid] == target:
            index = mid
            return index
        if array[mid] < target:
            left = mid
        if array[mid] > target:
            right = mid
    if abs(array[left] - target) <= abs(array[right] - target):
        index = left
    else:
        index = right
    return index


print(k_closet([1, 2, 3, 4, 7, 8, 9, 11], 10, 5))
