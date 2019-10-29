##Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# class Solution:
# def searchRange(self, nums: List[int], target: int) -> List[int]:
class Solution:
    def searchRange(self,nums, target):
        if nums is None or target is None or len(nums) == 0 :
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        res = []
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            res.append(left)
        elif nums[right] == target:
            res.append(right)
        else:
            res.append(-1)

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            res.append(right)
        elif nums[left] == target:
            res.append(left)
        else:
            res.append(-1)
        return res

nums = [5,7,7,8,8,10]
target = 6