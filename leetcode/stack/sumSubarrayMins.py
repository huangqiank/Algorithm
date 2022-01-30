##907. 子数组的最小值之和
# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
# 由于答案可能很大，因此 返回答案模 10^9 + 7 。
# 示例 1：
# 输入：arr = [3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
# 示例 2：
# 输入：arr = [11,81,94,43,3]
# 输出：444

## 递增的stack数列
##  找第一个比它小的index
## -1 1 3 4 0
class Solution:
    def sumSubarrayMins(self, arr):
        stack = []
        res = 0
        arr.append(0)
        for i in range(len(arr)):
            while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                tmp = stack.pop()
                if len(stack) == 0:
                    pre = -1
                else:
                    pre = stack[-1]
                res+= arr[tmp]*(i-tmp)*(tmp-pre)
            stack.append(i)
        return res
