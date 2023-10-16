##213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

class Solution:
    def rob(self, nums):
        # dp[i][0] = max(dp[i-1][0] , dp[i-1][1])
        # dp[i][1] = dp[i-1][0] + nums[i]
        n = len(nums)
        nums1 = nums[1:n]
        nums2 = nums[0:n - 1]
        dp = [[0 for i in range(2)] for j in range(n - 1)]
        dp[0][0] = 0
        dp[0][1] = nums1[0]
        for i in range(1, n - 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums1[i]
        max_l = max(dp[n - 1][0], dp[n - 1][1])
        dp[0][0] = 0
        dp[0][1] = nums2[0]
        for i in range(1, n - 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums2[i]
        max_l = max(max_l, dp[n - 1][0], dp[n - 1][1])
        return max_l
