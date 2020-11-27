##Given an unsorted array nums,
##reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
##Example:
##Input: nums = [3,5,2,1,6,4]
##Output: One possible answer is [3,5,1,6,2,4]

##[1,3,2,5,4,7,6]
##
def wiggleSort(nums):
    nums.sort()
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


nums = [3, 5, 2, 1, 6, 4]
print(wiggleSort(nums))
