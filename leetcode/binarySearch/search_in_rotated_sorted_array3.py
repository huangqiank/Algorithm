##Suppose an array sorted in ascending order is rotated
##at some pivot unknown to you beforehand.
##(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
##You are given a target value to search.
# If found in the array return true, otherwise return false.
##Example 1:
##Input: nums = [2,5,6,0,0,1,2], target = 0
##Output: true
##Example 2:
##Input: nums = [2,5,6,0,0,1,2], target = 3
##Output: false
##Follow up:
##This is a follow up problem to Search in Rotated Sorted Array,
# where nums may contain duplicates.
##Would this affect the run-time complexity? How and why?


##[4,5,6,7,0,1,2]

###
# 若大于 0 则第一段
# 若小于 0 则第二段

##target <mid:
##若mid 第一段 则 target 可能第一段可能第二段
##若mid第二段 则target在第二段

## target >mid:
##若mid第一段 则target第一段
##若mid第二段则target可能第一段，可能第二段



##mid >l

##l在左边
## > l 则  r = mid

##l在右边
##mid

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l + 1 < r:
        mid = int((l + r) / 2)
        if nums[mid] == target:
            return mid
        if nums[l] == nums[mid]:
            l+=1
            continue
        if nums[mid] > nums[l]:







nums = [1, 3, 1, 1, 1]
target = 3
print(search(nums, target))
