def divide_two_number(a, b):
    max_num = 2 ** 31 - 1
    min_num = -2 ** 31
    if a == 0 or b == 0:
        return 0
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        flag = -1
    else:
        flag = 1
    i = 0
    while a << i <= b:
        i += 1
    res = 0
    while i >= 0:
        if b >= (a << i):
            res += 1 << i
            b -= a << i
        i -= 1

    if flag == -1:
        return max(min_num, -res)
    return min(max_num, res)


def myPower(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
    n = abs(n)
    if n % 2 == 0:
        return myPower(x * x, n / 2)
    return x * myPower(x, n - 1)


def mysqrt(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    right = int(x / 2)
    left = 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if mid * mid == x:
            return mid
        if mid ^ 2 < x:
            left = mid
        if mid ^ 2 > x:
            right = mid

    if left * left > x:
        return left - 1
    if left * left == x:
        return left
    if right * right <= x:
        return right
    if right * right > x:
        return right - 1


def closed_num(nums, x):
    left = 0
    right = len(nums)
    while left + 1 < right:
        mid = int((left + right) / 2)
        if mid * mid == x:
            right = mid
        if mid > x:
            right = mid
        if mid < x:
            left = mid
    if left * left == x:
        return left
    if right * right == x:
        return right
    if abs(left * left - x) < abs(right * right - x):
        return left
    return right


def find_k_closed_nums(nums, target, k):
    index = closed_num(nums, target)
    res = []
    left = 0
    right = len(nums)

    while k > 0:
        res.append(index)
        k-=1
        if index < 0 :

            res.extend(nums[index+1,min(k+index,right)])



