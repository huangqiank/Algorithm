import collections


class Solution:
    # dp[(i,j)]= dp[(j,i-j)]
    def lenLongestFibSubseq(self, arr):
        dp = collections.defaultdict(lambda: 2)
        n = len(arr)
        ans = 0
        num_index = {x: i for i, x in enumerate(arr)}
        for i in range(n):
            for j in range(i):
                t = num_index.get(arr[i] - arr[j], None)
                if t != None and t < j:
                    dp[(j, i)] = dp[(t, j)] + 1
                    ans = max(dp[j, i], ans)
        if ans >= 3:
            return ans
        return 0

idx = collections.defaultdict(int)
print(idx[1])
print(idx[2])

s=[1,2,3,3]
print(s.pop(-1))
print(s)
a={1:2,2:3}
print(a.pop(1))
print(a)


idx = {}
print(idx.get("a",0))