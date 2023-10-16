##239. 滑动窗口最大值
#给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#返回 滑动窗口中的最大值 。
#示例 1：
#输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
#输出：[3,3,5,5,6,7]
#解释：
#滑动窗口的位置                最大值
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k >= n:
            return [max(nums)]
        num_dict = {}
        for i in range(k):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = [i]
            else:
                num_dict[nums[i]].append(i)
        res = [max(num_dict.keys())]
        pre_max = res[0]
        i = 0
        j = k
        while j < n:
            if nums[j] not in num_dict:
                num_dict[nums[j]] = [j]
            else:
                num_dict[nums[j]].append(j)
            if i >= num_dict[nums[i]][-1]:
                del num_dict[nums[i]]
            if pre_max not in num_dict:
                pre_max = max(num_dict.keys())
                res.append(pre_max)
            else:
                pre_max = max(pre_max, nums[j])
                res.append(pre_max)
            i += 1
            j += 1
        return res
