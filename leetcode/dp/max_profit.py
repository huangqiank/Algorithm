# 买卖股票的最佳时机
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 示例 1：
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。


class Solution:
    def maxProfit(self, prices) :
        n = len(prices)
        min_dp = [0 for i in range(n)]
        ans = -float("inf")
        min_dp[0] = prices[0]
        for i in range(1, n):
            if prices[i] >= min_dp[i - 1]:
                min_dp[i] = min_dp[i - 1]
            else:
                min_dp[i] = prices[i]
            ans = max(ans, prices[i] - min_dp[i])
        if i == 1:
            return 0
        return ans
s=Solution()
a= [7,1,5,3,6,4]
print(s.maxProfit(a))