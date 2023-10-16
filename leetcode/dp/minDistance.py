##72. Edit Distance
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        ## s[i] == s[j],   dp[i][j] = dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]
        ## s[i] != s[j],   dp[i][j] = dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1

        n = len(word1)
        m = len(word2)
        if n == 0:
            return m
        if m == 0:
            return n
        dp = [[0 for i in range(m)] for j in range(n)]
        if word1[0] == word2[0]:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for i in range(1, n):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, m):
            if word1[0] == word2[j]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j - 1] + 1

        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[n - 1][m - 1]


s = Solution()
a = "pneumonoultramicroscopicsilicovolcanoconiosis"
b = "ultramicroscopically"


##583. Delete Operation for Two Strings
# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
# In one step, you can delete exactly one character in either string.
# # Example 1:
# # Input: word1 = "sea", word2 = "eat"
# # Output: 2
# # Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for i in range(m)] for j in range(n)]
        if word2[0] == word1[0]:
            dp[0][0] = 1
        for i in range(1, n):
            if word2[0] == word1[i]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, m):
            if word1[0] == word2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return m + n - 2 * dp[n - 1][m - 1]


class Solution:
    def minDistance(self, word1, word2):
        n = len(word1)
        m = len(word2)
        dp = [[0 for i in range(m)] for j in range(n)]
        if word2[0] == word1[0]:
            dp[0][0] =1
        for i in range(1, m):
            if word2[i] == word1[0]:
                dp[0][i] = i
            else:
                dp[0][i] = dp[0][i - 1] + 1
        for j in range(1, n):
            if word1[j] == word2[0]:
                dp[j][0] = j
            else:
                dp[j][0] = dp[j - 1][0] + 1
        for i in range(1, n):
            for j in range(1, m):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[n-1][m-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m=len(word2)
        dp = [[0 for i in range(m)] for j in range(n)]
        if n == 0 :
            return m
        if m == 0 :
            return n
        if word1[0] != word2[0]:
            dp[0][0]=2
        for i in range(1,m):
            if word1[0] == word2[i]:
                dp[0][i] = i
            else:
                dp[0][i] = dp[0][i-1]+1
        for i in range(1,n):
            if word2[0] == word1[i]:
                dp[i][0] = i
            else:
                dp[i][0] = dp[i-1][0]+1
        for i in range(1,n):
            for j in range(1,m):
                if word1[i] ==word2[j]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j] +1 ,dp[i][j-1] +1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+2,dp[i-1][j] +1 ,dp[i][j-1]+1)
        return dp[n-1][m-1]


a = str(1231)
a= a.replace("1","9")

print(a.replace("1","9"))