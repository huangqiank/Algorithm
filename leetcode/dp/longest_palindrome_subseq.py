#给定一个字符串s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设s的最大长度为1000 。
#示例1:输入:
#"bbbab"
##输出：4
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp =[[0 for i in range(len(s))] for j in range(len(s))]
        n = len(s)
        for i in range(n-1,-1,-1):  ##n-2
            for j in range(i,n,1 ): ## n-1
                if i == j:
                    dp[i][j] =1
                    continue
                if s[i] ==s[j]:   ##n-1 ##n-2
                     dp[i][j] = dp[i+1][j-1] +2
                else:
                     dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]