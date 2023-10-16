##368. 最大整除子集
#给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
#answer[i] % answer[j] == 0 ，或
#answer[j] % answer[i] == 0
#如果存在多个有效解子集，返回其中任何一个均可。
#示例 1：
#输入：nums = [1,2,3]
#输出：[1,2]
#解释：[1,3] 也会被视为正确答案。


class Solution:
    def largestDivisibleSubset(self, nums):
        nums = sorted(nums)
        n = len(nums)
        dp = [(-1, 1) for i in range(n)]
        max_l = 0
        max_l_index = 0
        res = []
        for i in range(1, n):
            tmp = 1
            index = -1
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j][1] + 1 > tmp:
                        index = j
                        tmp = dp[j][1] + 1
            if tmp > max_l:
                max_l = tmp
                max_l_index = i
            dp[i] = (index, tmp)
        while max_l_index != -1:
            res.append(nums[max_l_index])
            max_l_index = dp[max_l_index][0]
        return res

nums = [1,2,4,8,3,6,12,24,48]

s= Solution()
print(s.largestDivisibleSubset(nums))