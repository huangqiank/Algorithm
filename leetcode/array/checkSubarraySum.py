##523. 连续的子数组和
#给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
#子数组大小 至少为 2 ，且
#子数组元素总和为 k 的倍数。
#如果存在，返回 true ；否则，返回 false 。
#如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终视为 k 的一个倍数。
#示例 1：
#输入：nums = [23,2,4,6,7], k = 6
#输出：true
#解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums, k):
        presum = 0
        presum_map = defaultdict(int)
        presum_map[0] = -1
        for i in range(len(nums)):
            presum += nums[i]
            m = presum % k
            if m in presum_map:
                if i - presum_map[m] >= 2:
                    return True
            else:
                presum_map[m] = i

        return False

s= Solution()
print(s.checkSubarraySum([0,0],1))