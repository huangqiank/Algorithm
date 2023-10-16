###444. 序列重建
# 验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。
# 序列 org 是 1 到 n 整数的排列，其中 1 ≤ n ≤ 104 。
# 重建是指在序列集 seqs 中构建最短的公共超序列。
# （即使得所有  seqs 中的序列都是该最短序列的子序列）。
# 请你确定是否只可以从 seqs 重建唯一的序列，且该序列就是 org 。
# 示例 1：
# 输入：org = [1,2,3], seqs = [[1,2],[1,3]]
# 输出：false
# 解释：[1,2,3] 不是唯一的可重建序列，[1,3,2] 也是一个有效的可重建序列。
# 示例 2：
# 输入：org = [1,2,3], seqs = [[1,2]]
# 输出：false
# 解释：可重建序列只能是 [1,2] 。
# 示例 3：
# 输入：org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# 输出：true
# 解释：序列 [1,2]、[1,3] 和 [2,3] 可以从原始序列 [1,2,3] 唯一地重建。
# 示例 4：
# 输入：org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# 输出：true
# 提示：
# 1 <= n <= 10^4
# org 是 {1,2,...,n} 的一个排列
# 1 <= segs[i].length <= 10^5
# seqs[i][j] 符合 32 位整数范围
import collections


class Solution:
    def sequenceReconstruction(self, nums, sequences):
        indegrees = collections.defaultdict(int)
        adjacent = collections.defaultdict(list)
        num_set = set()
        for seq in sequences:
            num_set.add(seq[0])
            for i in range(len(seq) - 1):
                x = seq[i]
                y = seq[i + 1]
                indegrees[y] += 1
                adjacent[x].append(y)
                num_set.add(y)
        if len(num_set) != len(nums) or set(nums) != num_set:
            return False
        queue = []
        res = []
        for num in num_set:
            if num not in indegrees or indegrees[num] == 0 :
                queue.append(num)
        while queue:
            if len(queue) > q:
                return False
            num = queue.pop(0)
            res.append(num)
            for i in adjacent[num]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
        return res == nums


s = Solution()
a= [1,2,3]
b = [[1,2],[1,3],[2,3]]


s= "A man, a plan, a canal: Panama"
print(list(s.replace(" ","").lower()))


class Solution2:
    def checkSubarraySum(self, nums, k):
        presum = 0
        presum_map = set()
        for i in range(len(nums)):
            presum += nums[i]
            m = presum % k
            if m in presum_map or (m == 0 and len(presum_map)) > 0 :
                return True
            presum_map.add(m)
        print(presum_map)
        return False
s = Solution2()
print(s.checkSubarraySum([23,2,4,6,6],7))