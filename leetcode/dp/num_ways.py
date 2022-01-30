# 276. 栅栏涂色
# 有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，请你按下述规则为栅栏设计涂色方案：
# 每个栅栏柱可以用其中 一种 颜色进行上色。
# 相邻的栅栏柱 最多连续两个 颜色相同。
# 给你两个整数 k 和 n ，返回所有有效的涂色 方案数 。
# 1，2，3

# 输入：n = 3, k = 2
# 输出：6
# 解释：所有的可能涂色方案如上图所示。注意，全涂红或者全涂绿的方案属于无效方案，因为相邻的栅栏柱
# 最多连续两个 颜色相同。

##                                 dp1        dp2
## 2 2*2  6, dp[n-1]*k - dp[n-1](最后两个一样，最后两个不一样)
## dp1[j] =  dp2[j-1]
##dp2[j] = dp1[j-1] *(n-1) + dp2[j-1] * (n-1)
class Solution89:
    def numWays(self, n: int, k: int) -> int:
        dp1 = [0 for i in range(n)]
        dp2 = [0 for i in range(n)]
        dp1[0] = k
        dp1[1] = k
        dp2[0] = k
        dp2[1] = k * (k - 1)
        for i in range(2, n):
            dp1[i] = dp2[i - 1]
            dp2[i] = dp1[i - 1] * (k - 1) + dp2[i - 1] * (k - 1)
        return dp1[n - 1] + dp2[n - 1]
s = Solution89()
print(s.numWays(4, 2))