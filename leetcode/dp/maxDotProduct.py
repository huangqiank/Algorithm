##1458. Max Dot Product of Two Subsequences
# Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
# Example 1:

# Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
# Output: 18
# Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
# Their dot product is (2*3 + (-2)*(-6)) = 18

class Solution:
    def maxDotProduct(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        max_dp = [[0 for i in range(m)] for j in range(n)]
        if n == 0 or m == 0:
            return 0
        max_dp[0][0] = nums1[0] * nums2[0]
        for i in range(1, m):
            max_dp[0][i] = max(nums1[0] * nums2[i], max_dp[0][i - 1])

        for i in range(1, n):
            max_dp[i][0] = max(nums1[i] * nums2[0], max_dp[i - 1][0])

        for i in range(1, n):
            for j in range(1, m):
                k = nums1[i] * nums2[j]
                max_dp[i][j] = max(k, max_dp[i - 1][j - 1], max_dp[i - 1][j],
                                   max_dp[i][j - 1], k + max_dp[i - 1][j - 1])
        return max_dp[n - 1][m - 1]


