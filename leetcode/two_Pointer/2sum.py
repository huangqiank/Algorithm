##Given an array of integers,
##return indices of the two numbers
##such that they add up to a specific target.

##You may assume that each input would have exactly one solution,
##and you may not use the same element twice.

##Example:

##Given nums = [2, 7, 11, 15], target = 9,

##Because nums[0] + nums[1] = 2 + 7 = 9,
##return [0, 1].

def twoSum(nums, target):
    if not nums:
        return
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] not in nums_dict:
            nums_dict[nums[i]] = [i]
        else:
            nums_dict[nums[i]].append([i])
    nums = sorted(nums)
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            if nums[i] == nums[j]:
                return nums_dict[nums[i]]
            return [nums_dict[nums[i]][0], nums_dict[nums[j]][0]]
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1


nums = [2, 11, 15,7]
target = 9
print(twoSum(nums, target))
