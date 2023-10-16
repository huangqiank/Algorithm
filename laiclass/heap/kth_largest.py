'''
Created on Sep 11, 2017

@author: qiankunhuang
'''

import heapq


def kth_Max(A, k):
    B = A[:k]
    heapq.heapify(B)
    for i in range(k, len(A), 1):
        if A[i] > B[0]:
            heapq.heappop(B)
            heapq.heappush(B, A[i])
    return B.pop(0)


b = [1, 2, 3, 4, 5, 10, -1]
print(kth_Max(b, 3))


class Solution21:
    def maxNonOverlapping(self, nums, target):
        pre_sum = {}
        pre_sum[0] = -1
        pre = 0
        cnt = 0
        index = -1
        for i in range(len(nums)):
            pre += nums[i]
            if pre - target in pre_sum:
                if pre_sum[pre - target] >= index:
                    cnt += 1
                    index = i
            pre_sum[pre] = i
        return cnt

nums = [-2,6,6]
target = 10
s = Solution21()
print(s.maxNonOverlapping(nums,target))
##max_heap h
##[-2,6,6]
##[5,4,1]
##[2,8]