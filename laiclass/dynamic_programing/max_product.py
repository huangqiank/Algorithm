'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
def maxProduct(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    globalMax = 0
    for i in range(1, n, 1):
        best = max(n - i, maxProduct(n - i))
        globalMax = max(globalMax, best * i)
    return globalMax


def maxProduct2(n):
    dp = [1 for i in range(n + 1)]
    for i in range(n + 1):
        curmax = 1
        for j in range(i):
            curmax = max(curmax, j * max(i - j, dp[i - j]))
        dp[i] = curmax
    return dp[n]


print(maxProduct2(8))









            
            

