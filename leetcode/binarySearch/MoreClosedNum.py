def kClosedNum(a, b, c):
    t = closedNum(a, b)
    left = t
    right = t + 1
    res = []

    while c > 0:
        if left < 0:
            res.extend(a[left:min(c + left, len(a) - 1)])
            return res
        if right > len(a) -1:
            while c > 0 :
                res.append(a[left])
                left -= 1
                c -= 1
            return res
        if abs(a[left] - b) <= abs(a[right] - b):
            res.append(a[left])
            left -= 1
            c -= 1
        else:
            res.append(a[right])
            right += 1
            c -= 1
    return res


def closedNum(a, b):
    left = 0
    right = len(a) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if a[mid] > b:
            right = mid
        if a[mid] < b:
            left = mid
        if a[mid] == b:
            return mid
    if abs(a[left] - b) <= abs(a[right] - b):
        return left
    return right


print(kClosedNum([1, 2, 3, 4, 7, 8, 9, 11], 10, 5))