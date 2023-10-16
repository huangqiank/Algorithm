###75. 颜色分类
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库的sort函数的情况下解决这个问题。
# 示例 1：
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：
# 输入：nums = [2,0,1]
# 输出：[0,1,2]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        q = len(nums) - 1
        self.quick_sort(nums, p, q)
        return nums

    def quick_sort(self, nums, p, q):
        if p < q:
            partiotn = self.compute(nums, p, q)
            self.quick_sort(nums, p, partiotn - 1)
            self.quick_sort(nums, partiotn + 1, q)

    def compute(self, nums, p, q):
        j = q - 1
        i = p
        while i < q:
            if nums[i] < nums[q]:
                j+=1
                nums[i], nums[j] = nums[j], nums[i]

            i += 1
        j += 1
        nums[j], nums[q] = nums[q], nums[j]
        return j
