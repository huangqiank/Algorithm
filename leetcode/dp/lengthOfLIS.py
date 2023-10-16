##300. 最长递增子序列
##给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#示例 1：
#输入：nums = [10,9,2,5,3,7,101,18]
#输出：4
#解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [(0,0) for i in range(len(nums))]
        n  = len(nums)
        dp[0] = (1,nums[0])
        if n == 0:
            return 0
        max_l=1
        for i in range(1,n):
            tmp= (1,nums[i])
            for j in range(i):
                if nums[i] > dp[j][1] and tmp[0] < 1 +dp[j][0]:
                    tmp = (1+ dp[j][0],nums[i])
            max_l =max(max_l,tmp[0])
            dp[i] = tmp
        return max_l



class Solution2:
    def lengthOfLIS(self, nums):
        d=[]
        n = len(nums)
        for i in range(n):
            if not d or  d[-1] < nums[i]:
                d.append(nums[i])
            else:
                index = self.binary_search(d,nums[i])
                d[index] = nums[i]
        return len(d)
    def binary_search(self,nums,target):
        l = 0
        r = len(nums)-1
        while l+1 < r:
            mid = int((l+r)/2)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        if nums[l] >= target:
            return l
        return r




s = Solution()
print(s.lengthOfLIS( [0,1,0,3,2,3]))




