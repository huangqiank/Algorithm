def binary_search(nums, a):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == a:
            return mid
        if nums[mid] < a:
            left = mid
        else:
            right = mid
    if nums[left] == a:
        return left
    if nums[right] == a:
        return right
    return -1


def closed_num(nums, a):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] == a:
            return mid
        if nums[mid] < a:
            left = mid
        if nums[mid] > a:
            right = mid
    if abs(nums[left] - a) < abs(nums[right] - a):
        return left
    return right


def matrix(nums, k):
    row_length = len(nums)
    col_length = len(nums[0])
    right = row_length * col_length - 1
    left = 0
    while left + 1 < right:
        mid = int((left + right) / 2)
        row = right / col_length
        col = right % col_length
        if nums[row][col] == k:
            return row, col
        if nums[row][col] < k:
            left = mid
        if nums[row][col] > k:
            right = mid
    row = left / col_length
    col = left % col_length
    if nums[row][col] == k:
        return row, col
    row = right / col_length
    col = right % col_length
    if nums[row][col] == k:
        return row, col
    return -1


def k_closed(nums, target, k):
    index = closed_num(nums, target)
    res = []
    left = index - 1
    right = index + 1
    res.append(nums[index])
    while len(res) < k and left >= 0 and right < len(nums):
        if abs(nums[left] - target) < abs(nums[right] - target):
            res.append(nums[left])
            left -= 1
        else:
            res.append(nums[right])
            right += 1
    if len(res) < k:
        if left < 0:
            res.append(nums[right:min(right + k - len(res), len(res))])
        if right > len(nums):
            res.append(nums[max(left + 1 - (k - len(res)), 0):left + 1])


def k_closed2(nums, target, k):
    index = closed_num(nums, target)
    res = []
    left = index
    right = index + 1
    while k > 0:
        if left < 0:
            res.extend(nums[right:right + k])
            return res
        if right >= len(nums):
            while k > 0:
                res.append(nums[left])
                left -= 1
                k -= 1
            return res
        if abs(nums[left] - target) < abs(nums[right] - target):
            res.append(left)
            k -= 1
            left -= 1
        else:
            res.append(right)
            k -= 1
            right += 1
    return res


class Solution():
    def closed_num(self, nums, a):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = int((left + right) / 2)
            if nums[mid] == a:
                return mid
            if nums[mid] < a:
                left = mid
            if nums[mid] > a:
                right = mid
        if abs(nums[left] - a) <= abs(nums[right] - a):
            return left
        return right

    def findClosestElements(self, arr, k, x):
        index = self.closed_num(arr, x)
        res = []
        left = index
        right = index + 1
        while k > 0:
            if left < 0:
                res.extend(arr[right:right + k])
                return res
            if right >= len(arr):
                while k > 0:
                    res.append(arr[left])
                    left -= 1
                    k -= 1
                res.sort()
                return res
            if abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                k -= 1
                left -= 1
            else:
                res.append(arr[right])
                k -= 1
                right += 1
            res.sort()
        return res


s = Solution()
arr = [1, 3]
k = 1
x = 2
print(s.findClosestElements(arr, k, x))


def closed_num(nums, target):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = (left + right) / 2
        if nums[mid] <= target:
            left = mid
        if nums[mid] > target:
            right = mid
    if abs(nums[left] - target) <= abs(nums[right] - target):
        return left
    return right


def find_k_closed_num(nums, target, k):
    index = closed_num(nums, target)
    left = index - 1
    right = index + 1
    res = []
    while len(res) < k and
