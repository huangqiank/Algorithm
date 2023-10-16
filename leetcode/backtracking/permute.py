##46. 全排列
#给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
## 示例 1：
#输入：nums = [1,2,3]
#输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#示例 2：
#输入：nums = [0,1]
#输出：[[0,1],[1,0]]
#示例 3：
#输入：nums = [1]
#输出：[[1]]

class Solution:
    def permute(self, nums):
        index = 0
        n= len(nums)
        self.res = []
        path =[]
        self.dfs(index,n,nums,path)
        return self.res
    def dfs(self,index,n,nums,path):
        if index == n :
            if path not in self.res:
                self.res.append(path.copy())
            return
        for i in range(n):
            if nums[i] not in path:
                path.append(nums[i])
                self.dfs(index+1,n,nums,path)
                path.pop()

class Solution2:
    def permute(self, nums):
        index = 0
        n= len(nums)
        self.res = []
        path =[]
        used = {}
        for i in nums:
            used[i] = -1
        self.dfs(index,n,nums,path,used)
        return self.res
    def dfs(self,index,n,nums,path,used):
        if index == n :
            self.res.append(path.copy())
            return
        for i in range(n):
            if used[nums[i]] == -1:
                path.append(nums[i])
                used[nums[i]] = 1
                self.dfs(index+1,n,nums,path,used)
                path.pop()
                used[nums[i]] = -1


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res
class Solution:
    def permuteUnique(self, nums):
