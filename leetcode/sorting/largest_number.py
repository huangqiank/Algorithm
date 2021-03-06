##Given a list of non negative integers, arrange them such that they form the largest number.
##Example 1:
##Input: [10,2]
##Output: "210"
##Example 2:
##Input: [3,30,34,5,9]
##Output: "9534330"
###根据第一个数字大的放前面，其次第二个数字大的放前面，
###长度

def largestNumber(nums):
    if not nums:
        return nums
    n = len(nums)
    for i in nums:
        if i != 0:
            return "".join(sort(nums, n))
    return "0"


def sort(nums, n):
    if n == 1:
        return [str(nums[0])]
    left = sort(nums[0:n // 2], n // 2)
    right = sort(nums[n // 2:], n - n // 2)
    return sort_merge(left, right, n // 2, n - n // 2)


def sort_merge(left, right, size1, size2):
    point1 = 0
    point2 = 0
    res = []
    while point1 < size1 and point2 < size2:
        a = str(left[0])
        b = str(right[0])
        c = a + b
        d = b + a
        if int(c) >= int(d):
            point1 += 1
            res.append(a)
            left.pop(0)
        else:
            point2 += 1
            res.append(b)
            right.pop(0)
    while point1 < size1:
        res.append(str(left[0]))
        left.pop(0)
        point1 += 1
    while point2 < size2:
        point2 += 1
        res.append(str(right[0]))
        right.pop(0)
    return res


a = [0,0]
print(largestNumber(a))
a = [0,30,90,1000,2]
print(largestNumber(a))
