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
