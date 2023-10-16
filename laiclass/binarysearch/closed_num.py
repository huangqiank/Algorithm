def closed_num(a, b):
    left = 0
    right = len(a) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if a[mid] == b:
            return mid
        if a[mid] < b:
            left = mid
        if a[mid] > b:
            right = mid

    if abs(a[left] - b) > abs(a[right] - b):
        return right
    return left


a = [1, 2, 3, 4, 5, 7, 10, 20]
print(closed_num(a, 19))


class Solution:
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - 1
        while l + 1 < r:
            mid = int((l + r) / 2)
            if arr[mid] >= x:
                r = mid
            else:
                l = mid
        res = []
        i = 0
        while i < k:
            if l < 0:
                res.append(arr[r])
                r += 1
                i += 1
                continue
            if r >= len(arr):
                res.append(arr[l])
                l -= 1
                i += 1
                continue
            if abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
                i += 1
            else:
                res.append(arr[r])
                r += 1
                i += 1
        return res
