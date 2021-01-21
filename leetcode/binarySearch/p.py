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
    right = len(nums) - 1
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
        k -= 1
        if index < 0:
            res.extend(nums[index - + 1, min(k + index, right)])


## a *2^i < b
##

def divide_two_number1(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0:
        return 0
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        flag = 1
    else:
        flag = -1
    i = 0
    res = 0
    while a << i < b:
        i += 1
    while i > 0:
        if a >> i < b:
            res += i
            b -= a >> i
            i -= 1
    if flag == -1:
        return -res
    return res


def find_first_last(nums, target):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    tmp1 = mid
    while nums[tmp1] == target and tmp1 >= 0:
        tmp1 -= 1
    tmp2 = mid
    while nums[tmp2] == target and tmp2 < len(nums):
        tmp2 += 1
    res = [tmp1 + 1, tmp2 - 1]
    return res


def find_duplicated(nums):
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    new = 0
    while True:
        new = nums[new]
        slow = nums[slow]
        if new == slow:
            return new
    return new


def more_closed_num(nums, target):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int(left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    if abs(nums[left] - target) < abs(nums[right] - target):
        return left
    return right


def my_sqrt(x):
    left = 0
    right = int(x / 2) + 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid
        else:
            right = mid
    if left * left <= x:
        return left
    if right * right <= x:
        return right
    if right * right > x:
        return left
    if left * left > x:
        return left - 1


def search_insert_position(nums, target):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] >= target:
        return left
    if nums[right] >= target:
        return right
    if nums[right] < target:
        return right + 1


def search_matrix(matrix, target):
    left = 0
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    right = len(matrix) * len(matrix[0]) - 1
    row = len(matrix[0])
    while left + 1 < right:
        mid = (left + right) / 2
        row_num = int(mid / row)
        col_num = mid % row
        if matrix[row_num][col_num] == target:
            return row_num, col_num
        if matrix[row_num][col_num] < target:
            left = mid
        else:
            right = mid
    if matrix[int(left / row)][left % row] == target:
        return left / row, left % row
    if matrix[int(right / row)][right % row] == target:
        return right / row, right % row
    return -1


def search_matrix2(matrix, target):
    row_num = len(matrix)
    col_num = len(matrix[0])
    m = len(matrix) - 1
    l = 0
    while 0 <= l < col_num and 0 <= m < row_num:
        if matrix[m][l] == target:
            return m, l
        if matrix[m][l] < target:
            l += 1
        else:
            m -= 1
    return -1


def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        if nums[left] + nums[right] == target:
            return left, right
        if nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    if nums[left] + nums[right] == target:
        return [left, right]
    return -1


def binary_search(nums, k):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == k:
            return mid
        if nums[mid] > k:
            right = mid
        else:
            left = mid
    return mid


def closed_num(nums, k):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == k:
            return mid
        if nums[mid] < k:
            left = mid
        else:
            right = mid
    if abs(nums[left] - k ) < abs(nums[right] - k ):
        return left
    return right



def