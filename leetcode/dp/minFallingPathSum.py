##1289. 下降路径最小和  II
# 给你一个 n x n 整数矩阵 arr ，请你返回 非零偏移下降路径 数字和的最小值。
# 非零偏移下降路径 定义为：从 arr 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
# 示例 1：
# 输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：13
# 解释：
# 所有非零偏移下降路径包括：
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# 下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。
# 示例 2：
# 输入：grid = [[7]]
# 输出：7


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if not grid :
            return
        n = len(grid)
        if n == 0:
            return 0
        if n == 1:
            return grid[0][0]
        dp = [[0 for i in range(n)] for j in range(n)]
        first = -1
        second = -1
        for i in range(n):
            dp[0][i] = grid[0][i]
            if first == -1:
                first = i
            elif dp[0][i] < dp[0][first]:
                second = first
                first = i
            elif dp[0][i] < dp[0][second]:
                second = i
        for i in range(1, n):
            next_first = -1
            next_second =-1
            for j in range(n):
                if j != first:
                    dp[i][j] = dp[i-1][first] + grid[i][j]
                else:
                    dp[i][j] = dp[i-1][second] + grid[i][j]
                if next_first == -1:
                    next_first = j
                elif dp[i][j] < dp[i][next_first]:
                    next_second = next_first
                    next_first = j
                elif dp[i][j] < dp[i][next_second]:
                    next_second = j
            first = next_first
            second = next_second
        return min(dp[n - 1])

