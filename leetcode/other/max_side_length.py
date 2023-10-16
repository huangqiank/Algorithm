##1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
# Example 1:
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
# Example 2:
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0

class Solution:
    ## d[i][j] = d[i-1][j] + d[i][j-1] + mat[i][j] - d[i-1][j-1]
    ## mat[i-k][j-k] = d[i][j] - d[i-k][j] - d[i][j-k]+ d[i-k][j-k]
    def cal_area(self, k, n, m, dp, threshold, ):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i - k < 0 or j - k < 0:
                    continue
                tmp = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                if tmp <= threshold:
                    return 1
        return 0

    def maxSideLength(self, mat, threshold):
        n, m = len(mat), len(mat[0])
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        dp[0][0] = mat[0][0]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + mat[i - 1][j - 1] - dp[i - 1][j - 1]

        l, r = 0, min(n, m)
        while l + 1 < r:
            k = int((l + r) / 2)
            if self.cal_area(k, n, m, dp, threshold) == 1:
                l = k
            else:
                r = k
        if self.cal_area(r, n, m, dp, threshold) == 1:
            return r
        return l
