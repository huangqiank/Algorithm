'''
Created on Jan 18, 2018

@author: qiankunhuang
'''
import heapq


def kthSmallestMatrix(matrix, k):
    n = len(matrix)
    res = []
    for i in range(n):
        heapq.heappush(res, (matrix[i][0], 0, matrix[i]))
    for i in range(k-1):
        a = heapq.heappop(res)
        if a[1] + 1 < len(a[2]):
            heapq.heappush(res, (a[2][a[1]+1], a[1]+1, a[2]))
    return heapq.heappop(res)


matrix = [[1, 3, 5, 7], [2, 4, 8, 9], [3, 5, 11, 15], [6, 8, 13, 18]]
print(kthSmallestMatrix(matrix, 6))
