'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
def Jump_game(A):
    if A is None or len(A) == 0:
        return True
    n = len(A)
    M=[False for i in xrange(len(A))]
    M[n-1] =True
    for j in xrange(len(A)-2,-1,-1):
        for i in xrange(A[j]+1):
            if i+j >=n or M[i+j]:
                    M[i] = True
                    break
    return M[0]


def jump_game(A):
    if A is None or len(A)==0:
        return True
    n= len(A)
    dp = [False for i in xrange(n)]
    dp[n-1]=True
    for j in xrange(n-2,-1,-1):
        for i in xrange(A[j]+1):
            if j+i<=n:
                if dp[j+i] is True: 
                    dp[j] = True
                    break
            else:
                dp[j] = True
    return dp[0]
    
print Jump_game([2,3,1,1,4])
print Jump_game([3,2,1,0,4])
        
                 