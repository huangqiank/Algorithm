##139. 单词拆分
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 示例 1：
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for j in range(1, n + 1):
            for i in range(j):
                if s[i:j] in wordDict and dp[i]:
                    dp[j] = 1
                    break
        return dp[n] ==1