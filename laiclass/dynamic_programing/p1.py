'''
Created on Jan 22, 2018

@author: qiankunhuang
'''
def max_product(n):
    dp =[1 for i in range(n+1)]
    for i in xrange(2,n+1,1):
        global_max = 1
        for j in range(0,i,1):
            global_max = max(global_max,j*max(i-j,dp[i-j]))
        dp[i] = global_max
    return dp[n]
print max_product(3)