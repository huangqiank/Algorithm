'''
Created on Oct 21, 2017

@author: qiankunhuang
'''
def longest_asc(lst):
    if not lst or len(lst) == 0:
        return 0
    n=len(lst)
    dp = [1 for i in xrange(len(lst))]
    global_max=1
    for i in xrange(1,n,1):
        if lst[i] > lst[i-1]:
            dp[i] = dp[i-1]+1
        global_max = max(global_max,dp[i])
    return global_max
    
