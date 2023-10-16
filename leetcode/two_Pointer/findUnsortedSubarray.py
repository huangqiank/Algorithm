##581. Shortest Unsorted Continuous Subarray
#Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
#Return the shortest such subarray and output its length.
#Example 1:
#Input: nums = [2,6,4,8,10,9,15]
#Output: 5
#Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        n = len(nums)
        min_val = nums[n-1]
        begin = 0
        end = -1
        for i in range(n):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                end = i
            if nums[n-i-1] <=min_val:
                min_val =nums[n-i-1]
            else:
                begin = n-i-1
        return end - begin +1


