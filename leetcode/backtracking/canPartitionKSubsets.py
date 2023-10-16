##698. 划分为k个相等的子集
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 示例 1：
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
class Solution:
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k != 0:
            return False
        self.target = sum(nums) / k
        self.nums = sorted(nums)
        if nums[-1] > self.target:
            return False
        begin = len(nums) - 1
        while begin >= 0 and nums[begin] == self.target:
            begin -= 1
            k -= 1
        subsets = [0 for i in range(k)]
        return self.dfs(begin, subsets)

    def dfs(self, begin, subsets):
        if begin < 0:
            return True
        selected = self.nums[begin]
        for i in range(len(subsets)):
            if selected + subsets[i] > self.target:
                continue
            subsets[i] += selected
            if self.dfs(begin - 1,  subsets):
                return True
            subsets[i] -= selected
            if subsets[i] == 0:
                return False
        return False

s = Solution()
print(s.canPartitionKSubsets([1,1,1,1,2,2,2,2],4))
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
print(s.canPartitionKSubsets([2,2,2,2,3,4,5],4))




class Solution4:
    def canPartitionKSubsets(self, nums, k):
        self.res = False
        if sum(nums) % k != 0:
            return self.res
        target = int(sum(nums) / k)
        self.nums = sorted(nums)
        self.k = k
        self.target = target
        tmp = 0
        index = 0
        used = [-1 for i in range(len(nums))]
        count = 0
        self.dfs(index, used, tmp, count)
        return self.res

    def dfs(self, index, used, tmp, count):
        if index >= len(self.nums) or tmp > self.target or count == self.k - 1:
            if count == self.k - 1:
                self.res = True
            return
        for i in range(index, len(self.nums)):
            if used[i] == -1:
                if tmp + self.nums[i] > self.target:
                    break
                if tmp + self.nums[i] < self.target:
                    used[i] = 1
                    self.dfs(index + 1, used, tmp + self.nums[i], count)
                    used[i] = -1
                if tmp + self.nums[i] == self.target:
                    used[i] = 1
                    self.dfs(index + 1, used, 0, count + 1)
                    used[i] = -1


s = Solution4()
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))


