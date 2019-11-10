'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
def getMax(lst):
    dp = [1 for i in range(len(lst))]
    if not lst or len(lst) == 0:
        return lst
    globalMax = 0
    for i in range(1, len(lst), 1):
        if lst[i] > lst[i - 1]:
            dp[i] = dp[i - 1] + 1
        globalMax = max(globalMax, dp[i])
    return globalMax


lst = [1, 2, 3, 45, 0, -1, 2, 1, -4]
print(getMax(lst))
    
    
    
    
    
    
    
    
                                                                                                                             
            

def getmax(lst):
    if not lst or len(lst)==0:
        return 0
    n = len(lst)
    dp = [1 for i in range(n)]
    global_max = 1
    for j in range(1,n,1):
        if lst[j] > lst[j-1]:
            dp[j]=dp[j-1]+1
        global_max = max(global_max,dp[j])
    return global_max


            
        
