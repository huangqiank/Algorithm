##给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 示例：
# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。


class Solution:
    def findLength(self, nums1, nums2):
        ## dp[i][j] if nums1[i] != nums2[j] ,  0
        ## if  nums[i] == nums[j] , 1 or + dp[i+1][j+1]
        n = len(nums1)
        m = len(nums2)
        tmp = 0
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            if nums1[i] == nums2[m - 1]:
                dp[i][m - 1] = 1
        for i in range(m):
            if nums1[n - 1] == nums2[i]:
                dp[n - 1][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if nums1[i] != nums2[j]:
                    dp[i][j] = 0
                elif dp[i + 1][j + 1] > 0:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    tmp = max(tmp, dp[i][j])
                else:
                    dp[i][j] = 1
                    tmp = max(tmp, dp[i][j])
        return tmp


a = [1, 2, 3, 2, 1]
b = [3, 2, 1, 4]
s = Solution()
print(s.findLength(a, b))


##if nums1[i] == nums2[j]:
##dp[i][j] = dp[i-1][j-1] +1
##else:
## 0
class Solution:
    def findLength(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        max_l = 0
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            if nums1[0] == nums2[i]:
                dp[0][i] = 1
        for i in range(n):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_l = max(max_l, dp[i][j])
        return max_l
