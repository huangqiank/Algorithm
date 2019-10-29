def findPeak(a):
    left = 0
    right = len(a) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if a[mid] > a[mid + 1] and a[mid] > a[mid - 1]:
            return mid
        if a[mid] < a[mid + 1]:
            left = mid
        if a[mid] < a[mid - 1] and a[mid] > a[mid + 1]:
            right = mid
    if a[left] < a[right]:
        return left
    else:
        return right


a = [1, 3, 1, 4, 5, 6, 7, 8, 9, 10, 2]
print(findPeak(a))

