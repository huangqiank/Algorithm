# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 说明：
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
# ]


class Solution:
    def combinationSum2(self, candidates, target):
        self.num_dict = {}
        self.num_list = []
        for num in candidates:
            if num not in self.num_dict:
                self.num_dict[num] = 1
                self.num_list.append(num)
            else:
                self.num_dict[num] += 1
        self.n = len(self.num_list)
        self.res = []
        self.target = target
        self.dfs(0, 0, [])
        return self.res

    def dfs(self, total, index, combination):
        if index >= self.n or total >= self.target:
            if total == self.target:
                self.res.append(combination)
            return
        tmp = self.num_list[index]
        for i in range(min(int(self.target / tmp) + 1, self.num_dict[tmp] + 1)):
            self.dfs(total + i * tmp, index + 1, combination + [tmp] * i)


d = []
s = Solution()

print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
