'''
Created on Feb 15, 2018

@author: qiankunhuang
'''
import heapq


## 去除k个最小数字，然后排好序
def kth_smallest(list, k):
    heapq.heapify(list)
    for i in range(k - 1):
        heapq.heappop(list)
    res = heapq.heappop(list)
    return res


# O(n+klogn)

def kth_largest(list, k):
    res = []
    A = list[:k]
    heapq.heapify(A)
    for i in range(k, len(list), 1):
        if list[i] > A[0]:
            heapq.heappop(A)
            heapq.heappush(A, list[i])
    return A[0]


b = [1, 2, 3, 4, 5, 10, -1]


##print(kth_largest(b,3))

def merge_kth_array(a):
    new = []
    res = []
    sum = 0
    for i in a:
        sum += len(i)
    for list in a:
        heapq.heappush(res, (list[0], 0, list))
    while sum > 0:
        c = heapq.heappop(res)
        new.append(c[0])
        if c[1] + 1 > len(c[2]) - 1:
            sum -= 1
        else:
            heapq.heappush(res, (c[2][c[1] + 1], c[1] + 1, c[2]))
            sum -= 1
    return new


matrix = [[1, 3, 5, 7], [2, 4, 8, 9], [3, 5, 11, 15], [6, 8, 13, 18]]


##print(merge_kth_array(matrix))


def kth_largest(list, k):
    res = []
    A = list[:k]
    heapq.heapify(A)
    for i in range(k, len(list), 1):
        if list[i] > A[0]:
            heapq.heappop(A)
            heapq.heappush(A, list[i])
    return A[0]


def kth_smallest(nums, k):
    sorted_nums = heapq.heapify(nums)
    for i in range(k - 1, 1):
        heapq.heappop(sorted_nums)
    num = heapq.heappop(sorted_nums)
    return num


def kth_largest(nums, k):
    sorted_nums = heapq.heapify(nums[:k])
    for i in range(k, len(nums), 1):
        if nums[k] > sorted_nums[0]:
            heapq.heappop(sorted_nums)
            heapq.heappush(sorted_nums, nums[k])
    return sorted_nums[0]


def kth_largest(nums, k):
    sorted_nums = heapq.heapify(nums[:k])
    for i in range(k, len(nums)):
        if nums[i] > sorted_nums[0]:
            heapq.heappop(sorted_nums)
            heapq.heappush(sorted_nums, nums[i])
    return sorted_nums[0]


