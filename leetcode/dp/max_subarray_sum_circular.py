# 给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
# 在此处，环形数组意味着数组的末端将会与开头相连呈环状。（
# 形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[ i +A.length] = C[i]）
# 此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。
# （形式上，对于子数组 C[i], C[ i +1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）
##i<j
# l = A[i:] +  a[:j]


##dp[N]


## A[i:n]
## A[:j]


class Solution:
    def maxSubarraySumCircular(self, A):
        n = len(A)
        ans = A[0]
        tmp = A[0]
        for i in range(1, n, 1):
            if ans > 0:
                ans += A[i]
            else:
                ans = A[i]
            tmp = max(tmp, ans)
        first_sum = [0 for i in range(n)]
        first_sum[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            first_sum[i] = first_sum[i + 1] + A[i]
        second_sum = [0 for i in range(n)]
        combine_sum = [0 for i in range(n - 1)]

        for j in range(0, n - 1, 1):
            if j == 0:
                second_sum[j] = A[0]
            else:
                second_sum[j] = second_sum[j - 1] + A[j]
            combine_sum[j] = second_sum[j] + max(first_sum[j + 1:])
        if len(A) >= 2:
            return max(tmp, max(combine_sum))
        return tmp


        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in xrange(N - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])
        leftsum = 0
        for i in xrange(N - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 2])
        return ans




class Solution(object):
    def maxSubarraySumCircular(self, A):
        N = len(A)
        ans = cur = -float("inf")
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        # ans is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2
        # rightsums[i] = sum(A[i:])
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + A[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])

        leftsum = 0
        for i in range(N - 2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i + 2])
        return ans

a = [1, -2, 3, -2]
# 3
b = [5, -3, 5]
# 10
c = [3, -1, 2, -1]
# 4
d = [3, -2, 2, -3]
# 3
f = [-2, -3, -1]
g = [-2]
s = Solution()
##print(s.maxSubarraySumCircular(b))
print(sum(b[2:]))
