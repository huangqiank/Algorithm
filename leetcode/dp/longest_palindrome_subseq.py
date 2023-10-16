# 给定一个字符串s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设s的最大长度为1000 。
# 示例1:输入:
# "bbbab"
##输出：4
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        n = len(s)
        for i in range(n - 1, -1, -1):  ##n-2
            for j in range(i, n, 1):  ## n-1
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:  ##n-1 ##n-2
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


class Solution2:
    def longestPalindrome(self, s: str):
        ##s[i] == s[j] and dp[i+1][j-1]
        ##dp[i][j] = 1
        ## dp[i][j] = 0
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        n = len(s)
        max_l = [0, ""]
        for i in range(n):
            dp[i][i] = 1
        for j in range(n):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j] and j-i == 1:
                    dp[i][j] = 1
                    if max_l[0] < 2:
                        max_l[0] = 2
                        max_l[1] = s[i:j + 1]
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    if max_l[0] < j - i + 1:
                        max_l[0] = j - i + 1
                        max_l[1] = s[i:j + 1]
        return max_l[1]
s = Solution2()
print(s.longestPalindrome("cbbd"))