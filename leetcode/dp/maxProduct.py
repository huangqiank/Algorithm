##152. Maximum Product Subarray
#Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
#The test cases are generated so that the answer will fit in a 32-bit integer.
#A subarray is a contiguous subsequence of the array.
#Example 1:
#Input: nums = [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.

class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        min_dp = [0 for i in range(n)]
        max_dp = [0 for i in range(n)]
        min_dp[0]= nums[0]
        max_dp[0] = nums[0]
        for i in range(1,n):
            if nums[i]>0:
                max_dp[i] = max(nums[i] * max_dp[i-1],nums[i])
                min_dp[i] = min(nums[i],nums[i] * min_dp[i-1])
            else:
                max_dp[i] = max(nums[i] * min_dp[i-1],nums[i])
                min_dp[i] = min(nums[i],nums[i] * max_dp[i-1])
        return max(max_dp)