##560. 和为 K 的子数组
#给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#示例 1：
#输入：nums = [1,1,1], k = 2
#输出：2
#示例 2：
#输入：nums = [1,2,3], k = 3
#输出：2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = defaultdict(int)
        i = 0
        n = len(nums)
        pre = 0
        pre_sum[0] = 1
        count =0
        while  i< n :
            pre += nums[i]
            count += pre_sum[pre-k]
            pre_sum[pre] += 1
            i+=1
        return count