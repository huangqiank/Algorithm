'''
Created on Jan 4, 2018

@author: qiankunhuang
'''


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


def merge(nums):
    if len(nums) == 0 or len(nums) == 1:
        return nums
    mid = int(len(nums) / 2)
    a = merge(nums[:mid])
    b = merge(nums[mid:])
    return merge_help(a, b)


def merge_help(a, b):
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            res.append(a[0])
            a.pop(0)
        else:
            res.append(b[0])
            b.pop(0)
    if len(a) != 0:
        res.extend(a)
    if len(b) != 0:
        res.extend(b)
    return res


def quick(nums):
    p = 0
    q = len(nums) - 1
    return quick_help(nums, p, q)


def quick_help(nums, p, q):
    if p > q:
        return nums
    d = partition(nums, p, q)
    quick_help(nums, p, d - 1)
    quick_help(nums, p, d + 1)
    return nums


def partition(nums, p, q):
    i = p - 1
    for j in range(p, q):
        if nums[j] < nums[q]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    i += 1
    nums[i], nums[q] = nums[q], nums[i]
    return i




