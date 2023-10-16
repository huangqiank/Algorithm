##221. Maximal Square
#Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#Example 1:
#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4
#Example 2:

#Input: matrix = [["0","1"],["1","0"]]
#Output: 1

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        max_l= 0
        dp =[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1
                    max_l = max(max_l,dp[i][j])
        return max_l * max_l



##1277. 统计全为 1 的正方形子矩阵
#给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
#示例 1：
#输入：matrix =
#[
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
#]
#输出：15
#解释：
#边长为 1 的正方形有 10 个。
#边长为 2 的正方形有 4 个。
#边长为 3 的正方形有 1 个。
#正方形的总数 = 10 + 4 + 1 = 15.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res= 0
        dp =[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) +1
                    res+= dp[i][j]
        return res