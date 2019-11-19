##Given an array nums of n integers and an integer target,
##find three integers in nums such that the sum is closest to target.
##Return the sum of the three integers.
##You may assume that each input would have exactly one solution.
##Example:
##Given array nums = [-1, 2, 1, -4], and target = 1.
##The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
def threeSumClosest(nums, target):
    dif = float('inf')
    nums = sorted(nums)
    n = len(nums)
    res = []
    if not nums or len(nums) < 3:
        return res
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return [nums[i], nums[l], nums[r]]
            if total < target:
                tmp = nums[l]
                if abs(target - total) < dif:
                    dif = abs(target - total)
                    res = [nums[i], nums[l], nums[r]]
                while nums[l] == tmp and l < r:
                    l += 1
                continue
            if total > target:
                tmp = nums[r]
                if abs(target - total) < dif:
                    dif = abs(target - total)
                    res = [nums[i], nums[l], nums[r]]
                while nums[r] == tmp and l < r:
                    r -= 1
                continue
    return res
nums = [0,0,0]
target = 1
print(threeSumClosest(nums, target))