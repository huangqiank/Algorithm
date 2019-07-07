'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
def max_product(n):
    if n<1:
        return 0
    if n ==1:
        return 1
    global_max=0
    for i in xrange(1,n,1):
        best = max(n-i,max_product(n-i))
        global_max= max(i*best, global_max)
    return global_max
print  max_product(5)

def max_product2(n):
    dp = [1 for i in xrange(n+1)]
    dp[1]=1
    for i in xrange(n+1):
        curmax=1
        for j in xrange(i): 
            curmax=max(curmax,j*max(i-j,dp[i-j]))
        dp[i] =curmax
    return dp[n]
print max_product2(2)








            
            

