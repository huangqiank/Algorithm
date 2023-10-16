##440. 字典序的第K小数字
# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
# 注意：1 ≤ k ≤ n ≤ 109。示例 :
# 输入:
# n: 13   k: 2
# 输出:10
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

class Solution:
    def get_count(self, a, n):
        cur = a
        next = a + 1
        ##[a,min(n+1),b]
        count = 0
        while cur <= n:
            count += min((n + 1), next) - cur
            cur *= 10
            next *= 10
        return count

    def findKthNumber(self, n, k):
        pre = 1
        p = 1
        while p < k:
            cnt = self.get_count(pre, n)
            if p + cnt > k:
                pre *= 10
                p += 1
            elif p + cnt <= k:
                pre += 1
                p += cnt
        return pre
