##Given an array nums of n integers and an integer target,
##are there elements a, b, c, and d in nums such that a + b + c + d = target?
##Find all unique quadruplets in the array which gives the sum of target.
##Note:
##The solution set must not contain duplicate quadruplets.
##Example:

##Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
##A solution set is:
##[
##  [-1,  0, 0, 1],
##  [-2, -1, 1, 2],
##  [-2,  0, 0, 2]
##]


def fourSum2(nums, target):
    res = []
    if not nums or len(nums) < 4:
        return res
    n = len(nums)
    nums = sorted(nums)
    for i in range(n - 3):
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue
            if j - i > 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = n - 1
            total = nums[i] + nums[j]
            while l < r:
                if total + nums[l] + nums[r] == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif total + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
    return res
## i 取不到 n-1 n-2 n-3
## j 取不到 n-1 n-2












class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res= []
        n = len(nums)
        for i in range(n):
            for j in range(n-1,i+2,-1):
                tmp = nums[i] + nums[j]
                if tmp + nums[j-1] + nums[j-2] <target :
                    break
                if  tmp + nums[i+1] + nums[i+2] > target:
                    continue
                k = i+1
                l = j-1
                while k < l :
                    if tmp + nums[k] + nums[l] == target:
                        if [nums[i],nums[j],nums[k],nums[l]] not in res:
                            res.append([nums[i],nums[j],nums[k],nums[l]])
                            k+=1
                            l-=1
                            continue
                    if  tmp + nums[k] + nums[l] < target:
                        k+=1
                    else:
                        l-=1
        return list(res)