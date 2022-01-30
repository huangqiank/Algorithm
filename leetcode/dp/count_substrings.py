# 647. 回文子串
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
# 示例 1：
###输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 示例 2：
# 输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa


class Solution:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        ## dp[i][j] = dp[i+1][j-1] +1
        ## dp[i][j] = dp[i+1][j-1]
        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 0
        total =0
        for i in range(n):
            for j in range(n):
                total+=dp[i][j]
        return total
s= Solution()
print(s.countSubstrings("aaa"))