##39. 组合总和
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
# 示例 1：
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 示例 2：
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 示例 3：
# 输入: candidates = [2], target = 1
# 输出: []


class Solution:
    def combinationSum(self, candidates, target):
        combination = []
        self.res = []
        self.n = len(candidates)
        self.candidates = candidates
        index = 0
        self.dfs(index, target, combination)
        return self.res

    def dfs(self, index, target, combination):
        if index == self.n or target <= 0:
            if target == 0:
                self.res.append(combination)
            return
        self.dfs(index + 1, target, combination)
        if target - self.candidates[index] >= 0:
            self.dfs(index + 1, target - self.candidates[index], combination + [self.candidates[index]])
            self.dfs(index, target - self.candidates[index], combination + [self.candidates[index]])


class Solution2:
    def combinationSum(self, candidates, target):
        self.n = len(candidates)
        self.candidates = candidates
        self.res = []
        self.target = target
        self.dfs(0, 0, [])
        res = []
        for i in self.res:
            if i not in res:
                res.append(i)
        return res

    def dfs(self, index, total, combination):
        if index == self.n or total >= self.target:
            if total == self.target:
                self.res.append(combination)
            return
        self.dfs(index + 1, total, combination)
        if total + self.candidates[index] <= self.target:
            self.dfs(index + 1, total + self.candidates[index], combination + [self.candidates[index]])
            self.dfs(index, total + self.candidates[index], combination + [self.candidates[index]])


class Solution3:
    def combinationSum(self, candidates, target):
        self.n = len(candidates)
        self.limit = []
        for i in candidates:
            self.limit.append(int(target / i))
        self.res = []
        combination = []
        self.candidates = candidates
        index = 0
        self.dfs(index, combination, target)
        return self.res

    def dfs(self, index, combination, target):
        if index == self.n or target <= 0:
            if target == 0:
                self.res.append(combination.copy())
            return
        for i in range(self.limit[index]+1):
            self.dfs(index + 1, combination + [self.candidates[index]] * i, target - self.candidates[index] * i)


s = Solution3()
a = [2, 3, 6, 7]
print(s.combinationSum(a, 7))

s = Solution2()
a = [2, 3, 6, 7]
print(s.combinationSum(a, 7))
