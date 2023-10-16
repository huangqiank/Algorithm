##47. 全排列 II
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# [1,2,1],
# [2,1,1]]
# 示例 2：

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


class Solution:
    def permuteUnique(self, nums):
        depth = 0
        path = []
        self.res = []
        num_cnt = {}
        for num in nums:
            num_cnt[num] = num_cnt.get(num, 0) + 1
        n = len(nums)
        self.dfs(path, depth, n, num_cnt)
        return self.res

    def dfs(self, path, depth, n, num_cnt):
        if depth == n and path not in self.res:
            self.res.append(path.copy())
            return
        for num in num_cnt.keys():
            if num_cnt[num] > 0:
                path.append(num)
                num_cnt[num] -= 1
                self.dfs(path, depth + 1, n, num_cnt)
                path.pop()
                num_cnt[num] += 1


class Solution2:
    def permuteUnique(self, nums):
        index = 0
        path = []
        self.res = []
        visited = {i: -1 for i in range(len(nums))}
        nums = sorted(nums)
        self.backtrack(path, index, nums, visited)
        return self.res

    def backtrack(self, path, index, nums, visited):
        if index == len(nums):
            self.res.append(path.copy())
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == -1:
                continue
            if visited[i] == -1:
                path.append(nums[i])
                visited[i] = 1
                self.backtrack(path, index + 1, nums, visited)
                path.pop()
                visited[i] = -1
s = Solution2()
print(s.permuteUnique([3,3,3,0]))