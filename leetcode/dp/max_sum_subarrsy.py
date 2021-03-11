def max_sum_subarray(nums):
    n = len(nums)
    ans = nums[0]
    tmp = 0
    for i in range(1, n, 1):
        if ans > 0:
            ans += nums[i]
        else:
            ans = nums[i]
        tmp = max(tmp, ans)
    return ans
