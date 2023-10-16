##496. 下一个更大元素 I
# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
# 示例 1：
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出：[-1,3,-1]
# 解释：nums1 中每个值的下一个更大元素如下所述：
# - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
# - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
from collections import defaultdict


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        num_dict = {}
        for i in reversed(nums2):
            while len(stack) != 0 and stack[-1] < i:
                stack.pop()
            if len(stack) == 0:
                num_dict[i] = -1
            else:
                num_dict[i] = stack[-1]
            stack.append(i)
        res = []
        for i in nums1:
            res.append(num_dict.get(i,-1))
        return res


class Solution12:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        stack = []
        i = len(s) -1
        max_num = 2147483647
        #98976534212
        ##6
        while i >= 0 :
            if len(stack) == 0 or s[i] >= stack[-1][0]:
                stack.append((s[i],i))
                i -= 1
                continue
            if s[i] < stack[-1][0]:
                j = self.find(s[i],stack)
                s[i],s[j] = s[j],s[i]
                s = s[:i+1] + sorted(s[i+1:])
                if int("".join(s)) > max_num:
                    print(int("".join(s)))
                    return -1
                return int("".join(s))
        return -1

    def find(self,target,l):
        for i in range(len(l)):
            if l[i][0] >target:
                return l[i][1]


class Solution1:
    def countPairs(self, deliciousness):
        num_set = set()
        t = 1
        for i in range(22):
            num_set.add(t)
            t *= 2
        deliciousness = sorted(deliciousness)
        print(deliciousness)
        print(sorted(num_set))
        num_cnt = defaultdict(int)
        ans = 0
        for food in deliciousness:
            for total in num_set:
                if num_cnt[total - food]> 0:
                    print(food,total - food)
                ans += num_cnt[total - food]
            num_cnt[food] += 1
        return ans


s= Solution1()
print(s.countPairs([1,0,1]))


