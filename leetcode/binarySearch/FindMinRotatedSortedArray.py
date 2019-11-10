##  a[mid] > a[0] and a[right]<a[0]     first     left = mid

## mid < a[0] and a[left] > a[0]   second    right = second


class Solution(object):
    def findMin(self, nums):
        if not nums or len(nums) == 0:
            return
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] >= nums[0] and nums[right] < nums[0]:
                left = mid
            elif nums[mid] < nums[0] and nums[left] >= nums[0]:
                right = mid
            else:
                break
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]


def FindMinRotatedSortednums(nums):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] >= nums[0] and nums[right] < nums[0]:
            left = mid
        elif nums[mid] < nums[0] and nums[left] >= nums[0]:
            right = mid
        else:
            break
    if nums[left] < nums[right]:
        return nums[left]
    else:
        return nums[right]


nums = [3, 1, 2]
print(FindMinRotatedSortednums(nums))
