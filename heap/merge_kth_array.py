'''
Created on Jan 19, 2018

@author: qiankunhuang
'''
import heapq


def mergeKthArray(a):
    sum = 0
    for i in a:
        sum += len(i)
    print(sum)
    res = []
    p = []
    for list in a:
        heapq.heappush(p, (list[0], 0, list))

    while sum > 0 :
        c = heapq.heappop(p)
        res.append(c[0])
        sum -=1
        if c[1]+1 < len(c[2]):
            heapq.heappush(p, (c[2][c[1]+1],c[1]+1,c[2]))

    return res


matrix = [[1, 3, 5, 7], [2, 4, 8, 9], [3, 5, 11, 15], [6, 8, 13, 18]]
print(kth_array(matrix))
