##78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]

## dfs
class Solution:
    def subsets(self, nums):
        self.res = []
        index = 0
        tmp = []
        self.generate_all(tmp, nums, index)
        return self.res

    def generate_all(self, tmp, nums, index):
        if index == len(nums):
            self.res.append(tmp.copy())
            return
        tmp.append(nums[index])
        self.generate_all(tmp, nums, index + 1)
        tmp.pop()
        self.generate_all(tmp, nums, index + 1)


## backtrack

class Solution2:
    def subsets(self, nums):
        self.res = []
        index = 0
        path = []
        self.backtrack(path, nums, index)
        return self.res

    def backtrack(self, path, nums, index):
        self.res.append(path)
        for j in range(index,len(nums)):
            ## 每一步，必须加一个点
            self.backtrack(path+nums[j],nums,j+1)

class Solution3:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(0, [])
        return res


##https://leetcode-cn.com/problems/subsets/solution/c-zong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-/

s = Solution3()
print(s.subsets([1, 2, 3]))


## for i in range(index,n):
##   path.append(nuns[i])
##   self.dfs()
##   path.pop()