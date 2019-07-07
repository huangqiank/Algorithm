'''
Created on Feb 15, 2018

@author: qiankunhuang
'''
def fib(n):
    dp = [0 for i in xrange(n)]
    dp[1] = 1
    for i in xrange(2,n,1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]
print fib(4)

def Jumpgame(A):
    n = len(A)
    dp = [False for i in xrange(n)]
    dp[n-1] =True
    for i in xrange(n-2,-1,-1):
        for  j in xrange(A[i]+1):
            if i+j >=n or dp[i+j] is True:
                dp[i] = True
                break
    return dp[0]
print Jumpgame([2,3,1,1,4])
print Jumpgame([3,2,1,0,4])

def longest_asc_array(list):
    n = len(list)
    dp = [1 for i in xrange(n)]
    global_length = 0 
    for i in xrange(1,n,1):
        if list[i]>list[i-1]:
            dp[i]=dp[i-1]+1
            global_length=max(global_length,dp[i])
    return global_length

def dict_word(input,dict):
    
    
    
        
        
        