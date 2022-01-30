##55. 跳跃游戏
#给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#数组中的每个元素代表你在该位置可以跳跃的最大长度。
#判断你是否能够到达最后一个下标。
#示例 1：
#输入：nums = [2,3,1,1,4]
#输出：true
#解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

class Solution:
    def canJump(self, nums):
        n = len(nums)
        right_most = 0
        for i in range(n):
            if i <=right_most:
                right_most = max(right_most , i + nums[i])
                if right_most >= n-1:
                    return True
        return  False


##45. 跳跃游戏 II
#给定一个非负整数数组，你最初位于数组的第一个位置。
#数组中的每个元素代表你在该位置可以跳跃的最大长度。
#你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#示例:
#输入: [2,3,1,1,4]
#输出: 2
#解释: 跳到最后一个位置的最小跳跃数是 2。
#     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#说明:
#假设你总是可以到达数组的最后一个位置。

class Solution:
    def jump(self, nums: List[int]) -> int:
        ##
        #right_most = 0
        #dp[j] = dp[i] + 1
        #if i + nums[i] > j
        #else -1
        n =len(nums)
        dp = [float("inf") for i in range(n)]
        dp[0] =0
        for  i in range(1,n):
            for j in range(i):
                if dp[j] !=float("inf") and j+nums[j] >=i:
                    dp[i] = min(dp[j]+1,dp[i])
        if dp[n-1] == float("inf"):
            return -1
        return dp[n-1]
