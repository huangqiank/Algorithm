'''
Created on Jan 19, 2018

@author: qiankunhuang
'''
def closest(a, b, c, k):
    matrix = []
    n=len(a)
    for i in range(len(a)):
        for j in range(len(b)):
            d = [[t**2+(a[i])**2+(b[j])**2,(a[i],b[j],t)] for t in c]
            matrix.append(d)
    return k_th( matrix, k)
import heapq
def k_th(matrix,k):
    n =len(matrix)
    res=[]
    for i in range(n):
        heapq.heappush(res,(matrix[i][0][0],matrix[i][0][1],0,matrix[i]))
    for j in range(k-1):
        pair = heapq.heappop(res)
        if pair[2]+1<len(pair[3]):
            heapq.heappush(res,(pair[3][pair[2]+1][0],pair[3][pair[2]+1][1],pair[2]+1,pair[3]))
    return heapq.heappop(res)[1]
A =[1,3,5]
B = [2,4]
C = [3,6]
print closest(A,B,C,2)         


class Solution(object):
   def kthSmallest(self,matrix,k):
        import heapq
        res=[]
        n=len(matrix)
        for i in range(n):
          heapq.heappush(res,(matrix[i][0][0],matrix[i][0][1],0,matrix[i]))
        for j in range(k-1):
          pair = heapq.heappop(res)
          if pair[2]+1<len(pair[3]):
            heapq.heappush(res,(pair[3][pair[2]+1][0],pair[3][pair[2]+1][1],pair[2]+1,pair[3]))
        return heapq.heappop(res)[1]
   def closest(self, a, b, c, k):
        matrix = []
        for i in range(len(a)):
          for j in range(len(b)):
              d = [[t*t+a[i]*a[i]+b[j]*b[j],(a[i],b[j],t)] for t in c]
              matrix.append(d)
        return self.kthSmallest(matrix,k)
    

            
        
    