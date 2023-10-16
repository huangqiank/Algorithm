# 491. Increasing Subsequences
# Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.
# The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.
# Example 1:

# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        index = 0
        tmp = []
        if len(nums) < 2:
            return []
        self.n = len(nums)
        self.nums = nums
        self.dfs(index, tmp)
        return self.res

    def dfs(self, index, tmp):
        if index == self.n:
            if len(tmp) >= 2 and tmp not in self.res:
                self.res.append(tmp)
            return
        if len(tmp) == 0 or tmp[-1] <= self.nums[index]:
            self.dfs(index + 1, tmp + [self.nums[index]])
        self.dfs(index + 1, tmp)


##############################################################
### 每一个dfs 只加一个数字
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, tmp):
            if len(tmp) > 1:
                res.append(tmp)
            pre = set()
            for index, num in enumerate(nums):
                if num not in pre:
                    pre.add(num)
                    dfs(nums[index + 1:], tmp + [num])
        dfs(nums,[])
        return res




