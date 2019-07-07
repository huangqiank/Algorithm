'''
Created on Dec 20, 2017

@author: qiankunhuang
'''
def coin_change(coins,amount):
    max = float("inf")
    dp = [0] + [max]*amount
    for i in xrange(1,amount+1,1):
        dp[i] = min(dp[i-c] if i-c>=0 else max for c in coins) + 1
    return dp[amount] if dp[amount] != max else -1
        
        