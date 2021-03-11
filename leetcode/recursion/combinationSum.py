# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1：
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#  [7],
#  [2,2,3]
# ]


## dfs(target,index,combination)

class Solution:
    def combinationSum(self, candidates, target):
        self.res = []
        self.n = len(candidates)
        self.candidates = candidates
        self.dfs(target, 0, [])
        return self.res

    def dfs(self, target, index, combination):
        if index == self.n or target <= 0:
            if target == 0:
                self.res.append(combination)
                print(self.res)
            return
        ## 不用
        self.dfs(target, index + 1, combination)
        ## 用
        if target - self.candidates[index] >= 0:
            combination.append(self.candidates[index])
            self.dfs(target - self.candidates[index], index, combination)
            combination.pop(-1)


class Solution2:
    def combinationSum(self, candidates, target):
        self.n = len(candidates)
        self.candidates = candidates
        self.res = []
        self.target = target
        self.dfs(0, 0, [])
        res= []
        for i in self.res:
            if i not  in res :
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


s = Solution2()
a = [2, 3, 6, 7]
print(s.combinationSum(a, 7))
