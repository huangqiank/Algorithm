# Given an array nums, write a function to move all 0's to the end of it '
# while maintaining the relative order of the non-zero elements.
##Example:

##Input: [0,1,0,3,12]
##Output: [1,3,12,0,0]
##Note:

##You must do this in-place without making a copy of the array.
# 3Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        j = 0
        while i < n:
            if nums[i] == 0:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        for t in range(j, n):
            nums[t] = 0
