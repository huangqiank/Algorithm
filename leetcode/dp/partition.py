##131. Palindrome Partitioning
#Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
#A palindrome string is a string that reads the same backward as forward.
#Example 1:
#Input: s = "aab"
#Output: [["a","a","b"],["aa","b"]]
#Example 2:


class Solution:
    def partition(self, s: str):
        n = len(s)
        dp = [[-1 for i in range(n)] for j in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    dp[i][j] = 1
                    continue
                if dp[i + 1][j - 1] ==1 and s[i] == s[j]:
                    dp[i][j] = 1

        print(dp)
        self.dp = dp
        self.s = s
        self.res = []
        self.tmp = []
        self.dfs(0)
        return self.res

    def dfs(self, index):
        if index == len(self.s):
            self.res.append(self.tmp.copy())
            return
        for i in range(index, len(self.s)):
            if self.dp[index][i] == 1:
                self.tmp.append(self.s[index:i + 1])
                self.dfs(i + 1)
                self.tmp.pop()
s = Solution()
print(s.partition("aab"))
## 23
## 14
