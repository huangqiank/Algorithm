#Given an array of integers that is already sorted in ascending order,
#find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that
#they add up to the target, where index1 must be less than index2.




def twoSum(nums,target):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        if nums[left] + nums[right] == target:
            return [left,right]
        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    if nums[left] + nums[right] == target:
        return [left,right]
    return -1


