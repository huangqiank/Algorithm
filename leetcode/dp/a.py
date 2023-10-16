# 给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
# 返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，
# r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。
# 输入：[
#    [-1,0],
#    [0,-1]
# ]
# 输出：[0,1,0,1]
# 解释：输入中标粗的元素即为输出所表示的矩阵


class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float("inf") for i in range(n)]
        dp[0] = 0
        if n == 0:
            return 0
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                if dp[i] != float("inf") and i + nums[i] >= j:
                    dp[j] = min(dp[j], dp[i] + 1)
        if dp[n - 1] == float("inf"):
            return -1
        return dp[n - 1]

a={1:2,5:1,3:1,2:3}
print(sorted(a.items(), key = lambda x:(x[1],x[0])))

print("a".isalpha())
print("A".lower())