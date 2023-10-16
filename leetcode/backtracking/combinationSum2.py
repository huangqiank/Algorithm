####给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。 
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
#
# [[1,2,2],
# [5]
# ]


class Solution:
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        self.res = []
        nums_cnt = {}
        for i in candidates:
            nums_cnt[i] = nums_cnt.get(i, 0) + 1
        self.nums = list(nums_cnt.keys())
        self.n = len(self.nums)
        self.limit = [min(nums_cnt[num], int(target / num)) for num in self.nums]
        combination = []
        index = 0
        self.dfs(index, target, combination)
        return self.res

    def dfs(self, index, target, combination):
        if index == self.n or target <= 0:
            if target == 0:
                self.res.append(combination)
            return
        for i in range(self.limit[index] + 1):
            self.dfs(index + 1, target - self.nums[index] * i, combination + [self.nums[index]] * i)


candidates = [2, 5, 2, 1, 2]
target = 5
s = Solution()
print(s.combinationSum2(candidates, target))
