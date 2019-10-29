'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fib2(n):
    res=[0,1]
    if n >=2 :
        fib2_help(n,res)
    return res[n]
def fib2_help(n,res):
    for i in range(2,n+1,1):
        res.append(res[i-1]+res[i-2])

def fib3(n):
    if n==0 or n==1:
        return 0
    dp = [1 for i in range(n+1)]
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1,1):
        dp[i] =dp[i-1]+dp[i-2]
    return dp[n]
print(fib(4))
print(fib2(4))
print(fib3(4))
    
    
    