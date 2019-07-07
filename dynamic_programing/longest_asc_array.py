'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
def get_max(lst): 
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
    
lst = [1,2,3,45,0,-1,2,1,-4]
print get_max(lst)
    
    
    
    
    
    
    
    
                                                                                                                             
            

def getmax(lst):
    if not lst or len(lst)==0:
        return 0
    n = len(lst)
    dp = [1 for i in xrange(n)]
    global_max = 1
    for j in xrange(1,n,1):
        if lst[j] > lst[j-1]:
            dp[j]=dp[j-1]+1
        global_max = max(global_max,dp[j])
    return global_max


            
        
            
    
        