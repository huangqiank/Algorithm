###90. 子集 II
#给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
#解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#示例 1：
#输入：nums = [1,2,2]
#输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#示例 2：
#输入：nums = [0]
#输出：[[],[0]]

class Solution:
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        index = 0
        self.res =[]
        path = []
        self.backtrack(path,index,nums)
        return self.res
    def backtrack(self,path,index,nums):
        self.res.append(path)
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.backtrack(path + [nums[i]],i+1,nums)

class Solution2:
    def subsetsWithDup(self, nums):
        self.res=[]
        path = []
        index= 0
        nums = sorted(nums)
        self.dfs(index,path,nums)
    def dfs(self,index,path,nums):
        if index == len(nums):
            if path not in self.res:
                self.res.append(path.copy())
            return
        path.append(nums[index])
        self.dfs(index+1,path,nums)
        path.pop()
        self.dfs(index+1,path,nums)

s=Solution()
print(s.subsetsWithDup([1,2,2]))
## for i in range(index,n):
##   if use[i]== -1:
##
##