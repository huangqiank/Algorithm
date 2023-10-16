##1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
# Example 1:

# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0 for i in range(m)] for j in range(n)]
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, n):
            if text1[i] == text2[0]:
                dp[i][0] = 13
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, m):
            if text2[i] == text1[0]:
                dp[0][i] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n - 1][m - 1]


s = Solution()
print(s.longestCommonSubsequence("acb", "abc"))


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0 for i in range(m)] for j in range(n)]
        if n == 0 or m == 0:
            return 0
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, m):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, n):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n - 1][m - 1]
