
##给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
# 现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
# 如果存在这样的分法，请返回 True ；否则，返回 False 。
# 示例 1：
# 输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# 输出：true
# 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10)


class Solution:
    def canArrange(self, arr, k):
        num_dict = {}
        num_list = []
        for num in arr:
            t = num % k
            if t in num_dict:
                num_dict[t] += 1
            else:
                num_dict[t] = 1
                num_list.append(t)
        if 0 in num_dict:
            if num_dict[0] % 2 != 0:
                return False
        for i in num_list:
            if i == 0:
                continue
            if k - i not in num_dict:
                return False
            if num_dict[i] != num_dict[k - i]:
                return False
        return True
