##22. 括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
# 输入：n = 1
# 输出：["()"]
### ), only r< l
## ( all case is fine

class Solution:
    def generateParenthesis(self, n):
        l = 0
        r = 0
        self.res = []
        combination = []
        self.n = n
        self.dfs(l, r, combination)
        return self.res

    def dfs(self, l, r, combination):
        if r == self.n:
            if l == self.n:
                self.res.append(combination)
            return
        if r < l:
            self.dfs(l, r + 1, combination + [")"])
        if l < self.n:
            self.dfs(l + 1, r, combination + ["("])
