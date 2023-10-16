##712. Minimum ASCII Delete Sum for Two Strings
# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str):
        n = len(s1)
        m = len(s2)
        dp = [[0 for i in range(m)] for j in range(n)]
        if n == 0:
            total = 0
            for i in s2:
                total += ord(i)
            return total
        if m == 0:
            total = 0
            for i in s1:
                total += ord(i)
            return total
        if s1[0] == s2[0]:
            dp[0][0] = 0
        else:
            dp[0][0] = ord(s1[0]) + ord(s2[0])
        total = ord(s2[0])
        for i in range(1,m):
            if s1[0] == s2[i]:
                dp[0][i] = total
            else:
                dp[0][i] = dp[0][i-1] + ord(s2[i])
            total += ord(s2[i])
        total = ord(s1[0])
        for i in range(1, n):
            if s1[i] == s2[0]:
                dp[i][0] = total
            else:
                dp[i][0] = dp[i - 1][0] + ord(s1[i])
            total += ord(s1[i])
        for i in range(1, n):
            for j in range(1, m):
                if s1[i] == s2[j]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + ord(s1[i]), dp[i][j - 1] + ord(s2[j]))
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i - 1][j], ord(s2[j]) + dp[i][j - 1],
                                   ord(s2[j]) + ord(s1[i]) + dp[i - 1][j - 1])
        return dp[n - 1][m - 1]

print(chr(ord("a") + 1))
print(chr(97))
print(ord("z"))