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


print(jumpGame([2, 3, 1, 1, 4]))
print(jumpGame([3, 2, 1, 0, 4]))
print(jumpGame([1, 1, 1, 1, 1]))
print(jumpGame([1, 1, 1, 1, 0]))


