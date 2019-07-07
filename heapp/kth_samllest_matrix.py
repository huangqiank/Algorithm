'''
Created on Jan 18, 2018

@author: qiankunhuang
'''
import heapq
def k_th(matrix,k):
    n =len(matrix)
    res=[]
    for i in range(n):
        heapq.heappush(res,(matrix[i][0],0,matrix[i]))
    for j in range(k-1):
        pair = heapq.heappop(res)
        if pair[1]+1<len(pair[2]):
            heapq.heappush(res,(pair[2][pair[1]+1],pair[1]+1,pair[2]))
    return heapq.heappop(res)[0]
matrix=[[1,  3,   5,  7],[2,  4,   8, 9],[3,  5, 11, 15],[6,  8, 13, 18]]
print k_th(matrix,6)            
            
            
        
    