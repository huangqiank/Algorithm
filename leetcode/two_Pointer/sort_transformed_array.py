##Given a sorted array of integers nums and integer values a, b and c.
##Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.
##The returned array must be in sorted order.
##Expected time complexity: O(n)
##Example 1:
##Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
##Output: [3,9,15,33]
##Example 2:
##Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
##Output: [-23,-5,1,7]
##计算中间值m
##若a>0,则根据|x-m|正序排序
##若a<0,则根据|x-m|倒序排序
##第一次遍历找到 m ,
# 若有i，j 开始遍历
def sortTransformedArray(nums, a, b, c):
    res = []
    if not nums or len(nums) == 0:
        return res
    if a == 0:
        for i in nums:
            res.append(b * i + c)
        if b >= 0:
            return res
        if b < 0:
            res.reverse()
            return res
    mid = b / (-2 * a)
    index = 0
    for i in range(len(nums)):
        if nums[i] < mid:
            index = i
        if nums[i] >= mid:
            break
    l = index
    r = index + 1
    while l >= 0 and r < len(nums):
        if abs(nums[l] - mid) < abs(nums[r] - mid):
            res.append(a * nums[l] * nums[l] + b * nums[l] + c)
            l -= 1
        else:
            res.append(a * nums[r] * nums[r] + b * nums[r] + c)
            r += 1
    while l >= 0:
        res.append(a * nums[l] * nums[l] + b * nums[l] + c)
        l -= 1
    while r < len(nums):
        res.append(a * nums[r] * nums[r] + b * nums[r] + c)
        r += 1
    if a > 0:
        return res
    res.reverse()
    return res


nums = [-4, -2, 2, 4]
a = -1
b = 3
c = 5
print(sortTransformedArray(nums, a, b, c))
