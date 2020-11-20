'''
Created on Jan 4, 2018

@author: qiankunhuang
'''


def merge_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    mid = len(nums) / 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    merge_sort_help(left, right)
    return merge_sort_help(left, right)


def merge_sort_help(left, right):
    res = []
    while len(left) != 0 or len(right) != 0:
        if left[0] <= right[0]:
            res.append(left[0])
        else:
            res.append(right[0])
    if len(left) != 0:
        res.extend(left)
    if len(right) != 0:
        res.extend(right)
    return res


def quick(nums):
    left = 0
    right = len(nums) - 1
    quick_help(nums, left, right)
    return nums


def quick_help(nums, left, right):
    if left < right:
        partition = compute_partition(nums, left, right)
        quick_help(nums, left, partition - 1)
        quick_help(nums, partition + 1, right)


def compute_partition(nums, left, right):
    i = left - 1
    p = left
    while p < right:
        if nums[left] < nums[right]:
            i += 1
            nums[i], nums[left] = nums[left], nums[i]
        p += 1
    i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i


def merge_sort(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    mid = len(nums) / 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return combine(left, right)


def combine(left, right):
    res = []
    while len(left) != 0 or len(right) != 0:
        if left[0] < right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)
    if len(left) != 0:
        res.extend(left)
    if len(right) != 0:
        res.extend(right)
        return res


def quick(nums):
    left = 0
    right = len(nums) - 1
    quick_help(left, right, nums)
    return nums


def quick_help(left, right, nums):
    if left > right:
        return nums
    p = parttion(left, right, nums)
    quick_help(left, p - 1, nums)
    quick_help(p + 1, right, nums)
    return nums


def parttion(left, right, nums):
    i = left - 1
    while left < right:
        if nums[left] < nums[right]:
            i += 1
            nums[left], nums[i] = nums[i], nums[left]
        left += 1

    i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i


