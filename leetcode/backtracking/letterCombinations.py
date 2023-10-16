##17. 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例 1：

# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
class Solution:
    def letterCombinations(self, digits: str):
        self.nums_str = {}
        if not digits or len(digits) == 0 or digits == "":
            return []
        self.nums_str["1"] = []
        self.nums_str["2"] = ["a", "b", "c"]
        self.nums_str["3"] = ["d", "e", "f"]
        self.nums_str["4"] = ["g", "h", "i"]
        self.nums_str["5"] = ["j", "k", "l"]
        self.nums_str["6"] = ["m", "n", "o"]
        self.nums_str["7"] = ["p", "q", "r", "s"]
        self.nums_str["8"] = ["t", "u", "v"]
        self.nums_str["9"] = ["w", "x", "y", "z"]
        self.res = []
        self.digits = digits
        index = 0
        self.n = len(digits)
        combination = ""
        self.dfs(index, combination)
        return self.res

    def dfs(self, index, combination):
        if index == self.n:
            self.res.append(combination)
            return
        if self.digits[index] == "1":
            self.dfs(index+1,combination)
        else:
            for s in self.nums_str[self.digits[index]]:
                self.dfs(index + 1, combination + s)


s= Solution()
print(s.letterCombinations("123"))