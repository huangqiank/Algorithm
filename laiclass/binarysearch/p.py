'''
Created on Feb 16, 2018

@author: qiankunhuang
'''


def binary_search(nums, k):
    n = len(nums)
    left = 0
    right = n - 1
    while left + 1 < right:
        mid = int(left + right) / 2
        if nums[mid] == k:
            return mid
        if nums[mid] < k:
            left = mid
        if nums[mid] > k:
            right = mid
    if nums[left] == k:
        return left
    if nums[right] == k:
        return right


def closed_nums(nums, k):
    n = len(nums)
    left = 0
    right = n - 1
    while left + 1 < right:
        mid = int(left + right) / 2
        if nums[mid] == k:
            return mid
        if nums[mid] < k:
            left = mid
        if nums[mid] > k:
            right = mid
    if abs(nums[left] - k) < abs(nums[right] - k):
        return left
    else:
        return right


def k_closed(nums, target, k):
    index = closed_nums(nums, target)
    res = [nums[index]]
    left = index
    right = index + 1
    while k > 0:
        if right > len(nums) - 1:
            res.extend(nums[left - k + 1:left + 1])
        if left < 0:
            res.extend(nums[right:right + k])
        if abs(nums[left] - target) <= abs(nums[right] - target):
            res.append(nums[left])
            left -= 1
            k -= 1
        if abs(nums[left] - target) > abs(nums[right] - target):
            res.append(nums[right])
            right += 1
            k -= 1
    return res
