'''
Created on Sep 10, 2017

@author: qiankunhuang
'''
import heapq
class  Heap:
    def __init__(self):
        self.size=0
        self.arr=[]
    
def kth_Min(input,k):
    A=input[:len(input)-k+1]
    heapq.heapify(A)
    for j in range(len(input)-k+1,len(input),1):
        if input[j] > A[0]:
            heapq.heappop(A)
            heapq.heappush(A,input[j])
    return A[0]
b = [1,2,3,4,5,10,-1]
print (kth_Min(b,3))