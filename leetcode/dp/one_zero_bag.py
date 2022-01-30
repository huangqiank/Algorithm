# 有N件物品和一个容量为V的背包。第i件物品的费用是c[i]，价值是w[i]。
# 求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
# 输入格式
# 第一行两个整数，N,M空格隔开，分别表示物品数量和背包容积。
# 接下来有N行,每行两个整数vi,wi,空格隔开,分别表示第i件物品的体积和价格
# 输出格式
# 输出一个整数，表示最大价值。
# 数据范围
# 0<N,M<1000
# 0<vi,wi<1000
# 输入样例
# 4 5
# 1 2
# 2 4
# 3 4
# 4 5
# 输出样例：
# 8
##其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大
##v=20，w={5，6，3，7，8}，p={6，7，4，8，9}，则最大价值为23
## 6+8+9

class solution:
    def k_napsack(self, v, w, m):
        ## dp[i][m] = dp[i-1][m-w[j]] + v[j]
        n = len(w)
        dp = [[0 for i in range(m + 1)] for i in range(n)]
        for i in range(0, m + 1):
            if w[0] <= i:
                dp[0][i] = v[0]
        for i in range(1, n):
            for j in range(1, m + 1):
                if j >= w[i]:
                    dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][m]

    def k_napsack2(self, v, w, m):
        n = len(w)
        dp = [0 for i in range(m + 1)]
        ## 把第一个商品先放进去
        for i in range(0, m + 1):
            if w[0] <= i:
                dp[i] = v[0]
        for i in range(1, n):
            for j in range(m, -1, -1):
                if j >= w[i]:
                    dp[j] = max(dp[j - w[i]] + v[i], dp[j])
                else:
                    dp[j] = dp[j]
        return dp[m]


# 有N 种物品和一个容量m的背包，每种物品都有无限件可用。
# 第i种物品的费用是w[i]，价值是v[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，
# 且价值总和最大。
## {indedx:count}
## dp[]
class solution:
    def all_apsack(self, v, w, m):
        n = len(w)
        dp = [0 for i in range(m + 1)]
        for j in range(m):
            if j >= w[j]:
                dp[j] = int(j / w[j]) * v[j]
        for i in range(1, n):
            for j in range(1, m + 1):
                if j >= w[i]:
                    dp[j] = max(dp[j], dp[j - w[i]] + v[i])
                else:
                    dp[j] = dp[j]
        return dp[m]
