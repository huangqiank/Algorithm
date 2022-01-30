###1060. 有序数组中的缺失元素
# 现有一个按 升序 排列的整数数组 nums ，其中每个数字都 互不相同 。
# 给你一个整数 k ，请你找出并返回从数组最左边开始的第 k 个缺失数字。
# 示例 1：
# 输入：nums = [4,7,9,10], k = 1
# 输出：5
# 解释：第一个缺失数字为 5 。
# 示例 2：

# 示例 2：
# 输入：nums = [4,7,9,10], k = 3
# 输出：8
# 解释：缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8

class Solution:
    def missingElement(self, nums, k):
        n = len(nums)
        l = 0
        r = n - 1
        while l + 1 < r:
            mid = int((l + r) / 2)
            dif = nums[mid]-nums[0]- mid
            if dif >= k:
                r = mid
            else:
                l = mid
        if nums[r] - nums[0] - r< k:
            t = k - (nums[r] - nums[0] - r)
            return nums[r] + t
        if nums[l] - nums[0] -l < k:
            t=k- (nums[l] - nums[0] -l)
            return nums[l ] + t
        if nums[l] - nums[0] -l >=k:
            t= (nums[l] - nums[0] -l)- k
            return nums[l]-t


s = Solution()
print(s.missingElement( [1,2,4], 3))






