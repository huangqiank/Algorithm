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