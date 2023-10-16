'''
Created on Oct 9, 2017

@author: qiankunhuang
'''


##每次可以走的步数在list里面，看是否可以从0走到n
def jumpGame(A):
    if not A or len(A) == 0:
        return A
    n = len(A)
    dp = [False for i in range(n)]
    dp[-1] = True
    for i in range(n - 2, -1, -1):
        for j in range(A[i] + 1):
            if i + j >= n or dp[i + j]:
                dp[i] = True
                break
    return dp[0]

class Solution:
    def canJump(self, nums) -> bool:
        ##dp[i] =1
        ##dp[j] and j+ s[j]> i
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] =1
        for i in range(1,n):
            for j in range(i):
                if dp[j] and j+nums[j] >= i:
                    dp[i]= 1
                    break
        return dp[n-1] ==1

print(jumpGame([2, 3, 1, 1, 4]))
print(jumpGame([3, 2, 1, 0, 4]))
print(jumpGame([1, 1, 1, 1, 1]))
print(jumpGame([1, 1, 1, 1, 0]))

##david  22.8---23.1    3.5   /// 24.7----25.1     ///
##agg    23.8----24.1   2   ///  25.2 ---25.8   ////

###  23.8月出国     
##   25.1----25.2 出国