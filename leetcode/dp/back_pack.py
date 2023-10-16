##92 · 背包问题预发布
# 在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A_{i}A i
​  # 你不可以将物品进行切割。
# 样例
# 样例 1：
# 输入：
# 数组 = [3,4,8,5]
# backpack size = 10
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """

    def back_pack(self, m: int, a):
        dp = [0 for i in range(m + 1)]
        dp[0] = 1
        max_l = 0
        for s in a:
            for i in range(m, -1, -1):
                if i == s:
                    dp[i] = 1
                    max_l = max(max_l, i)
                if i > s and dp[i - s] == 1:
                    dp[i] = 1
                    max_l = max(max_l, i)
        return max_l


##for s in a:
##    for i in range(m,-1,-1) 只用一次


# 125 · 背包问题（二）
# 有 n 个物品和一个大小为 m 的背包. 给定数组 A 表示每个物品的大小和数组 V 表示每个物品的价值.
# 问最多能装入背包的总价值是多大?
# A[i], V[i], n, m 均为整数
# 你不能将物品进行切分
# 你所挑选的要装入背包的物品的总大小不能超过 m
# 每个物品只能取一次
# m <= 1000m<=1000\
# len(A),len(V)<=100len(A),len(V)<=100
# 样例 1：输入：
# m = 10
# A = [2, 3, 5, 7]
# V = [1, 5, 2, 4]
# 输出：
# 9

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @param v: Given n items with value V[i]
    @return: The maximum value
    """

    def back_pack_i_i(self, m: int, a, v):
        a_v = {}
        for i in range(len(a)):
            a_v[i] = v[i]
        dp = [0 for i in range(m + 1)]
        for i in range(len(a)):
            for j in range(m, -1, -1):
                if a[i] == j:
                    dp[j] = a_v[i]
                if j > a[i] and dp[j - a[i]]:
                    dp[j] = max(dp[j], dp[j - a[i]] + a_v[i])
        return max(dp)


##440 · 背包问题 III
# 给定 n 种物品, 每种物品都有无限个. 第 i 个物品的体积为 A[i], 价值为 V[i].
# 再给定一个容量为 m 的背包. 问可以装入背包的最大价值是多少?
##输入: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10
# 输出: 15
# 解释: 装入三个物品 1 (A[1] = 3, V[1] = 5), 总价值 15

class Solution:
    """
    @param a: an integer array
    @param v: an integer array
    @param m: An integer
    @return: an array
    """

    def back_pack_i_i_i(self, a, v, m):
        dp = [0 for i in range(m + 1)]
        a_v = {}
        for i in range(len(a)):
            a_v[i] = v[i]
        for i in range(m + 1):
            for j in range(len(a)):
                if i == a[j]:
                    dp[i] = max(dp[i], a_v[j])
                if i > a[j] and dp[i - a[j]]:
                    dp[i] = max(dp[i], a_v[j] + dp[i - a[j]])
        return max(dp)


##562 · 背包问题 IV

# 给出 n 个物品, 以及一个数组, nums[i]代表第i个物品的大小, 保证大小均为正数并且没有重复, 正整数 target 表示背包的大小, 找到能填满背包的方案数。
# 每一个物品可以使用无数次

##输入: nums = [2,3,6,7] 和 target = 7
# 输出: 2
# 解释:
# 方案有:
# [7]
# [2, 2, 3]

class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    ##[223]
    ##[322]
    def backPackIV(self, nums, target):
        dp = [0 for i in range(target + 1)]
        for i in nums:
            for j in range(target + 1):
                if j == i:
                    dp[j] += 1
                if j > i and dp[j - i]:
                    dp[j] += dp[j - i]
        return dp[target]


##563 · 背包问题 V

#给出 n 个物品, 以及一个数组, nums[i] 代表第i个物品的大小, 保证大小均为正数, 正整数 target 表示背包的大小, 找到能填满背包的方案数。
#每一个物品只能使用一次


class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
# write your code here
        dp = [0 for i in range(target+1)]
        for i in nums:
            for j in range(target,-1,-1):
                if j == i:
                    dp[j] +=1
                if j > i and dp[j-i]:
                    dp[j] += dp[j-i]
        return dp[target]

