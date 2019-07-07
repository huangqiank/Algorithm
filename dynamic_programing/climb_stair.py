'''
Created on Dec 20, 2017

@author: qiankunhuang
'''
def climb(n):
    dp=[1 for i in xrange(n+1)]
    dp[1]=1
    dp[2]=2
    for i in xrange(3,n+1,1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
print climb(10)


    
    
    