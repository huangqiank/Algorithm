# 你有 k 个 非递减排列 的整数列表。
# 找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
# 示例 1：

# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释：
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 示例 2：
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]
# 示例 3：
# 输入：nums = [[10,10],[11,11]]
# 输出：[10,11]
# 示例 4：
# 输入：nums = [[10],[11]]
# 输出：[10,11]
# 示例 5：
# 输入：nums = [[1],[2],[3],[4],[5],[6],[7]]
# 输出：[1,7]


import heapq


class Solution:
    def smallestRange(self, nums):
        h = []
        left = 0
        right = 0
        max_num = -float("inf")
        for i in nums:
            h.append((i[0], i, 0))
            max_num = max(max_num, i[0])
        heapq.heapify(h)
        while len(h) != 0:
            min_num, l, index = heapq.heappop(h)
            if max_num - min_num < right - left:
                right = max_num
                left = min_num
            if index + 1 == len(l):
                break
            next = l[index + 1]
            max_num = max(max_num, next)
            heapq.heappush(h, (next, l, index + 1))
        return right - left
