###216. 组合总和 III
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k: int, n: int):
        self.n = 9
        self.k = k
        combination = []
        self.res = []
        index = 0
        target = n
        self.limit = [1] * 9

        self.dfs(index, combination, target)
        return self.res

    def dfs(self, index, combination, target):
        if index == self.n or len(combination) >= self.k or target <= 0:
            if len(combination) == self.k and target == 0:
                self.res.append(combination)
            return
        for i in range(self.limit[index] + 1):
            self.dfs(index + 1, combination + [index + 1] * i, target - i * (index + 1))



## s[i:j] = i,i+1 ..... j-1
## s[j-1:i-1 :-1] = s[j-1]
##s[0:3] == s[2:-1:-1]

s= "abc"
print(s[0:0])
print(s[0:2])
print(s[0:2][::-1])
print(list(s))