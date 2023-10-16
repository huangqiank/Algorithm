##131. 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。
# 示例 1：
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
# 输入：s = "a"
# 输出：[["a"]]

class Solution:
    def partition(self, s: str):
        index = 0
        partitions = []
        self.res = []
        self.dfs(index, partitions, s)
        return self.res

    def dfs(self, index, partitions, s):
        if index >= len(s):
            res = []
            for i in range(len(partitions)):
                if i == 0:
                    res.append(s[0:partitions[i]])
                else:
                    res.append(s[partitions[i - 1]:partitions[i]])
            if partitions[-1] != len(s):
                res.append((s[partitions[-1]::]))
            self.res.append(res)
            return
        for i in range(index, len(s) + 1):
            if i == 0:
                continue
            if len(partitions) == 0:
                tmp = s[0:i]
                if tmp == tmp[::-1]:
                    self.dfs(i + 1, partitions + [i], s)
            else:
                begin = partitions[-1]
                tmp = s[begin:i]
                if tmp == tmp[::-1]:
                    self.dfs(i + 1, partitions + [i], s)


class Solution2:
    def partition(self, s: str):
        ## dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        self.s = s
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
        index = 0
        partition = []
        self.dp = dp
        self.n = len(s)
        self.res = []
        self.dfs(index, partition)
        return self.res

    def dfs(self, index, partition):
        if index == self.n:
            self.res.append(partition)
            return
        for j in range(index, self.n):
            if self.dp[index][j] == 1:
                self.dfs(j + 1, partition + [self.s[index:j + 1]])


s = Solution2()
print(s.partition("abbab"))
## abbba a
