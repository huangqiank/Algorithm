def two_sum(nums, k):
    if not nums:
        return
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] not in nums_dict:
            nums_dict[nums[i]] = [i]
        else:
            nums_dict[nums[i]].append(i)
    l = 0
    r = len(nums) - 1
    nums = sorted(nums)
    while l < r:
        if nums[l] + nums[r] == k:
            if nums[l] == nums[r]:
                return nums_dict[nums[l]]
            return [nums_dict[nums[l]][0], nums_dict[nums[r]][0]]
        if nums[l] + nums[r] < k:
            l += 1
        else:
            r -= 1
    return -1


def three_sum_smaller(nums, k):
    nums = sorted(nums)
    count = 0
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] + nums[i] == k:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1

            if nums[l] + nums[r] + nums[i] < k:
                count += r - l
                l += 1
            else:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
    return count


def three_sum(nums):
    nums = sorted(nums)
    res = []
    if not nums or len(nums) < 3:
        return
    n = len(nums)
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i - 1]:
            i += 1
        l = i + 1
        r = n - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] < 0:
                tmp = nums[l]
                while l < r and tmp == nums[l]:
                    l += 1
            if nums[i] + nums[l] + nums[r] > 0:
                tmp = nums[r]
                while l < r and tmp == nums[r]:
                    r -= 1
            if nums[i] + nums[l] + nums[r] == 0:
                res.append([nums[i], nums[l], nums[r]])
                tmp = nums[l]
                while nums[l] == tmp and l < r:
                    l += 1
                tmp = nums[r]
                while nums[r] == tmp and l < r:
                    r -= 1
                continue
    return res


def three_sum_closed(nums, target):
