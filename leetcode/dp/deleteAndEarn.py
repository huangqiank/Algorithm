##给你一个整数数组 nums ，你可以对它进行一些操作。

#每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

#开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。


##示例 1：
#输入：nums = [3,4,2]
#输出：6
#解释：
#删除 4 获得 4 个点数，因此 3 也被删除。
#之后，删除 2 获得 2 个点数。总共获得 6 个点数。
#示例 2：

#输入：nums = [2,2,3,3,3,4]
#输出：9
#解释：
#删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
#之后，再次删除 3 获得

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_count = {}
        for num in nums:
            nums_count[num] =  nums_count.get(num,0) + 1
        distinct_nums = sorted(list(nums_count.keys()))
        n = len(distinct_nums)
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][0] = 0
        dp[0][1] = distinct_nums[0] * nums_count[distinct_nums[0]]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            tmp =  distinct_nums[i] * nums_count[distinct_nums[i]]
            if distinct_nums[i] - distinct_nums[i-1] == 1:
                dp[i][1] = dp[i-1][0] +  tmp
            else:
                dp[i][1] = max(dp[i-1][0],dp[i-1][1]) + tmp
        return max(dp[n-1][0],dp[n-1][1])