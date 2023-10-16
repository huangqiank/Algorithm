#518 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。
# 示例 1：

# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
##

class Solution111:
    def coinChange(self, coins, amount):
        dp = [float("inf") for i in range(amount + 1)]
        dp[0] = 0
        for i in range(amount+1):
            tmp = float("inf")
            for coin in coins:
                if i >= coin:
                    tmp = min(dp[i - coin] + 1, tmp)
            if tmp != float("inf"):
                dp[i] = tmp
        if dp[amount] != float("inf"):
            return dp[amount]
        return -1
s= Solution111()
print(s.coinChange([1,2,5],11))0



##518. Coin Change 2
#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
#You may assume that you have an infinite number of each kind of coin.
#The answer is guaranteed to fit into a signed 32-bit integer.
## for coin in coins:
##   for i in amount:
##  不会重复计算 2+ 3 ， 3+2 只计算一次
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 :
            return 1
        dp = [0 for i in range(amount+1)]
        for coin in coins:
            for i in range(amount+1):
                if i == coin :
                    dp[i] += 1
                if i > coin and dp[i-coin]:
                    dp[i] += dp[i-coin]
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]