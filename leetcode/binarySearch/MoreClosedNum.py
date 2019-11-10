##找离数字c最近的k个数字

####有问题的

def closed_num(nums, k):
    left = 0
    right = len(nums) - 1
    while left + 1 < right:
        mid = int((left + right) / 2)
        if nums[mid] >= k:
            right = mid
        else:
            left = mid
    if abs(nums[left] - k) < abs(nums[right] - k):
        return left
    return right


def find_k_closed_nums(nums, target, k):
    index = closed_num(nums, target)
    print(index)
    left = index
    right = index + 1
    res = []
    while k > 0 and (right <= len(nums) - 1 or left >= 0):
        if left < 0:
            res.append(nums[right])
            right += 1
            k -= 1
        elif right > len(nums) - 1:
            res.append(nums[left])
            left -= 1
            k -= 1
        else:
            if abs(nums[left] - target) < abs(nums[right] - target):
                res.append(nums[left])
                left -= 1
                k -= 1
            else:
                res.append(nums[right])
                right += 1
                k -= 1
    return res




print(find_k_closed_nums([1,2,3,4,5],3,1))
print(find_k_closed_nums([1, 2, 3, 4, 7, 8, 9, 11], 10, 13))