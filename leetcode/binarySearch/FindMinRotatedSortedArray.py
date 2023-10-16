##  a[mid] > a[0] and a[right]<a[0]     first     left = mid

## mid < a[0] and a[left] > a[0]   second    right = second


###153. 寻找旋转排序数组中的最小值
##已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
##若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
##若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
##注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
##给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
##示例 1：
##输入：nums = [3,4,5,1,2]
##输出：1
##解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

class Solution:
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[0]:
                left = mid
            if nums[mid] < nums[0]:
                right = mid
            if nums[mid] == nums[0]:
                break
        if nums[left] < nums[right]:
            return nums[left]
        return nums[right]


##33. 搜索旋转排序数组
##整数数组 nums 按升序排列，数组中的值 互不相同 。
##在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
##给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
##示例 1：
##输入：nums = [4,5,6,7,0,1,2], target = 0
##输出：4


class Solution2:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1
        if target == nums[0]:
            return 0

        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[0]:
                if nums[mid] < target:
                    left = mid
                elif target > nums[0]:
                    right = mid
                elif target < nums[0]:
                    left = mid
            if nums[mid] < nums[0]:
                if nums[mid] > target:
                    right = mid
                elif target > nums[0]:
                    right = mid
                elif target < nums[0]:
                    left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
s= Solution2()
print(s.search([0,1,2],0))


def reverseWords( s: str):
    s = s.strip(" ").split(" ")
    i = len(s) - 1
    res = []
    while i >= 0:
        if s[i] == "":
            i -= 1
        else:
            res.append(s[i])
            i -= 1
    print(res)
    return " ".join(res)



def isStraight(nums):
        dif = 0
        nums = sorted(nums)
        flag = 0
        for i in range(5):
            if nums[i] == 0:
                dif += 1
                continue
            if i > 0 and nums[i] != 0 and nums[i] == nums[i - 1]:
                return False
            if nums[-1] - nums[i] + i - 4 <= dif:
                flag = 1
                continue
            return False
        if flag == 1 or dif == 5:
            return True
        return False
print(isStraight([4,7,5,9,2]))




