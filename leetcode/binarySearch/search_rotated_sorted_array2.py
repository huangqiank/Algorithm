##Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
##(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
##You are given a target value to search. If found in the array return true, otherwise return false.
##Example 1:
##Input: nums = [2,5,6,0,0,1,2], target = 0
##Output: true
##Example 2:
##Input: nums = [2,5,6,0,0,1,2], target = 3
##Output: false
##Follow up:
##This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
##Would this affect the run-time complexity? How and why?

## mid  >= left  mid在第一段
##  target >= mid  在第一段 left = mid
##  target < mid
## target >= left  在第一段   right =mid
## target < left  在第二段    left = mid


##mid <left mid在第二段
## target <= mid  在第二段  right = mid
## target > mid:
## target > left  在第一段 right = mid
## target <= left  在第二段   left = mid

def search(nums, target):
    if not nums or len(nums) == 0:
        return False
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[0]:
            if nums[mid] < target:
                left = mid
            elif nums[0] <= target:
                right = mid
            else:
                left = mid
            continue
        if nums[mid] < nums[0]:
            if nums[mid] >= target:
                right = mid
            elif nums[0] < target:
                right = mid
            else:
                left = mid
            continue

    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 4

print(search(nums, target))
