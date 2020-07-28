import math


def binarysearch(nums, a):
    left = 0
    right = len(nums) - 1
    n = len(nums)
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == a:
            return mid
        if nums[mid] > a:
            right = mid
        if nums[mid] < a:
            left = mid
    if nums[left] == a:
        return left
    if nums[right] == a:
        return right
    return -1


def first_occur(nums, a):
    left = 0
    right = len(nums) - 1
    n = len(nums)
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] <= a:
            left = mid
        if nums[mid] > a:
            right = mid
    if nums[left] == a:
        return left
    if nums[right] == a:
        return right
    return -1


def closed_num(nums, a):
    left = 0
    right = len(nums) - 1
    n = len(nums)
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == a:
            return mid
        if nums[mid] < a:
            left = mid
        if nums[mid] > a:
            right = mid
    if abs(nums[left] - a) < abs(nums[right] - a):
        return left
    return right


def matrix(nums, k):
    row_length = len(nums)
    column_length = len(nums[0])
    left = 0
    right = row_length * column_length - 1
    while left + 1 < right:
        mid = int(left + right) / 2
        row = mid / column_length
        column = mid % column_length
        if nums[row][column] == k:
            return row, column
        if nums[row][column] < k:
            left = mid
        if nums[row][column] > k:
            right = mid
    row = left / column_length
    column = left % column_length
    if nums[row][column] == k:
        return row, column
    row = right / column_length
    column = right % column_length
    if nums[row][column] == k:
        return row, column


def k_closed(nums, target, k):
    index = k_closet_help(nums, target)
    res = [index]
    left = index - 1
    right = index + 1
    while len(res) < k and left >= 0 and right <= len(nums) - 1:
        if abs(nums[left] - target) <= abs(nums[right] - target):
            res.append(left)
            left -= 1
        else:
            res.append(right)
            right += 1
    if len(res) < k:
        if left < 0:
            res.append(nums[right:])
        else:
            res.append(nums[:left+1])
    return res


def k_closet_help(nums, k):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == k:
            return mid
        if nums[mid] < k:
            left = mid
        if nums[mid] > k:
            right = mid
    if abs(nums[left] - k) < abs(nums[right] - k):
        return left
    return right



