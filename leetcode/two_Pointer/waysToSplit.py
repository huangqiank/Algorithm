##1712. Ways to Split Array Into Three Subarrays
#A split of an integer array is good if:
#The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
#The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
#Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.
#Example 1:
#Input: nums = [1,1,1]
#Output: 1
#Explanation: The only good way to split nums is [1] [1] [1].

##Input: nums = [1,2,2,2,5,0]
#Output: 3
#Explanation: There are three good ways of splitting nums:
#[1] [2] [2,2,5,0]
##[1] [2,2] [2,5,0]
#[1,2] [2,2] [5,0]
import bisect
from itertools import accumulate


class Solution:
    def waysToSplit(self, nums):
        #nums[i] < nums[j]-nums[i] < total - nums[j]
        #2*nums[i] < nums[j] < int(total + nums[i])/2
        mod = 10 ** 9 + 7
        n = len(nums)
        pre_sum =[0 for i in range(n) ]
        pre_sum[0] = nums[0]
        for i in range(1,n):
            pre_sum[i] = pre_sum[i-1] + nums[i]
        total = pre_sum[n-1]
        ans = 0
        for i in range(n):
            l = max(i+1,bisect.bisect_left(pre_sum,2*pre_sum[i]))
            ## can't choose
            r = min(n-1, bisect.bisect_right(pre_sum,int((total + pre_sum[i])/2)))
            ans= (ans+ max(0,r-l)) %mod
        return ans


##[1 ,2, 2250]
##[1,22,250]
##[12,22,50]
##2