##Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
##Find all unique triplets in the array which gives the sum of zero.
##Note:
##The solution set must not contain duplicate triplets.
##Example:
##Given array nums = [-1, 0, 1, 2, -1, -4],
##A solution set is:
##[
##  [-1, 0, 1],
##  [-1, -1, 2]
##]

def threeSum(nums):
    nums = sorted(nums)
    res = []
    if not nums or len(nums) < 3:
        return res
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
                tmp = nums[l]
                while nums[l] == tmp and l < r:
                    l += 1
                tmp = nums[r]
                while nums[r] == tmp and l < r:
                    r -= 1
                continue
            if nums[i] + nums[l] + nums[r] < 0:
                tmp = nums[l]
                while nums[l] == tmp and l < r:
                    l += 1
                continue
            if nums[i] + nums[l] + nums[r] > 0:
                tmp = nums[r]
                while nums[r] == tmp and l < r:
                    r -= 1
                continue

    return res
nums = [0,0,0]
print(threeSum(nums))
nums = [0,-1,1,2,-2]
print(threeSum(nums))

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums_hash = {}
    result = list()
    for num in nums:
        nums_hash[num] = nums_hash.get(num, 0) + 1
    if 0 in nums_hash and nums_hash[0] >= 3:
        result.append([0, 0, 0])

    neg = list(filter(lambda x: x < 0, nums_hash))
    pos = list(filter(lambda x: x >= 0, nums_hash))

    for i in neg:
        for j in pos:
            dif = 0 - i - j
            if dif in nums_hash:
                if dif in (i, j) and nums_hash[dif] >= 2:
                    result.append([i, j, dif])
                if dif < i or dif > j:
                    result.append([i, j, dif])

    return result



