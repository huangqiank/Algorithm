##Given an array of n positive integers and a positive integer s,
## find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead
import bisect


def minSubArrayLen(s, nums):
    if not nums or len(nums) == 0:
        return
    right = len(nums)
    left = 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if minSubArrayLen_help(s, nums, mid):
            right = mid
        else:
            left = mid
    if minSubArrayLen_help(s, nums, left):
        return left
    if minSubArrayLen_help(s, nums, right):
        return right
    return 0


def minSubArrayLen_help(s, nums, mid):
    n = len(nums)
    for i in range(0, n - mid + 1):
        if sum(nums[i:i + mid]) >= s:
            return True
    return False


nums = [2, 3, 1, 2, 4, 3]
s = 0
print(minSubArrayLen(s, nums))


def minSubArrayLen2(k, nums):
    i, r, res = 0, 0, float('inf')
    for j in range(len(nums)):
        r += nums[j]
        while r >= k:
            res = min(res, j - i + 1)
            r -= nums[i]
            i += 1
    return res if res != float('inf') else 0


###·全相加就可以得到单调递增数列
def minSubArrayLen3(s, nums):
    if not nums:
        return 0
    new = []
    res = float('inf')
    for i in range(1, len(nums)):
        new.append(nums[i] + nums[i - 1])
    new = [0] + new
    if new[-1] < s:
        return 0
    for j in range(1,len(nums)):
        if nums[j] >= s:
            ##二分查找相邻target的数字
            loc = bisect.bisect_left(nums.nums[j] - s)
            if nums[j] - nums[loc] >= s:
                res = min(res, j - loc)
                continue
            if loc > 0:
                res = min(res, j - loc + 1)
