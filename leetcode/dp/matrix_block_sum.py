##给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，
# 其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和：
# i - K <= r <= i + K, j - K <= c <= j + K
# (r, c) 在矩阵内。
# 示例 1：
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]


class Solution:
    def matrixBlockSum(self, mat, k):
        n = len(mat)
        m = len(mat[0])
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = sum([col[:j] for col in mat[:i]])
        ans = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = dp[min(i + k + 1,n)][min(j + k + 1,m)] - dp[max(i - k,0)][min(j + k + 1,m)] - dp[min(i + k + 1,n)][max(j - k,0)] + dp[max(i - k,0)][max(j - k,0)]
        return ans
