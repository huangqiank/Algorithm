##给定一个整数数组 A，返回 A 中最长等差子序列的长度。
# 回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k]
# 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。
# 并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。
# 示例 1：
# 输入：[3,6,9,12]
# 输出：4
# 解释：
# 最长的等差子序列是 [4,7,10]。
# 整个数组是公差为 3 的等差数列。
# 输入：[9,4,7,2,10]
# 输出：3
# 解释：
# 最长的等差子序列是 [4,7,10]。
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        max_ans = 1
        for i in range(1, len(A)):
            for j in range(i):
                dp[i][A[i] - A[j]] = dp[j].get(A[i] - A[j], 1) + 1
                max_ans = max(max_ans, dp[i][A[i] - A[j]])
        return max_ans


class Solution:
    def longestArithSeqLength(self, A):
        ans = 1
        dp = {}
        n = len(A)
        A_set = set(A)
        dp[(A[0], A[1])] = 2
        for i in range(1, n):
            for j in range(i):
                if A[j] - (A[i] - A[j]) in A_set:
                    dp[(A[j], A[i])] = dp.get((2 * A[j] - A[i], A[j]), 1) + 1
                    if ans < dp[(A[j], A[i])]:
                        ans = dp[(A[j], A[i])]
        print(dp)
        return max(ans, 2)


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2 for _ in range(n)] for _ in range(n)]
        idx = defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                pre = A[i] * 2 - A[j]
                if pre in idx:
                    dp[i][j] = dp[idx[pre]][i] + 1  # 以 A[i]  A[j]为结尾的等差数组
                res = max(res, dp[i][j])
            idx[A[i]] = i
        return res

        return max(ans, 2)


class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = [[2 for i in range(n)] for i in range(n)]
        idx = {}
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                pre = 2 * A[i] - A[j]
                if pre in idx:
                    dp[i][j] = dp[idx[pre][j]] + 1
                res = max(res, dp[i][j])
            idx[A[i]] = i
        return res
