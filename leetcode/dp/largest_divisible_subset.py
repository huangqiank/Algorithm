# 给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对(Si，Sj) 都要满足：Si % Sj = 0
# 或
# Sj % Si = 0。

# 如果有多个目标子集，返回其中任何一个均可。


# 输入: [1, 2, 3]
# 输出: [1, 2]
##[1,2,4,8]
##[a1,a2,a3,a4]
## a4/a3  a3/a2 a2/a1


class Solution4:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums = sorted(nums)
        dp = [1 for i in range(n)]
        max_length = 0
        nums_dict = {}
        end = 0
        for i in range(1, n):
            tmp = 0
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if tmp < dp[j]:
                        nums_dict[nums[i]] = nums[j]
                        tmp = dp[j]
            dp[i] = tmp + 1
            if max_length < dp[i]:
                max_length = dp[i]
                end = nums[i]
        res = [end]
        while end in nums_dict:
            end = nums_dict[end]
            res.append(end)
        return res


s = Solution4()
print(s.largestDivisibleSubset([1, 2, 3]))
