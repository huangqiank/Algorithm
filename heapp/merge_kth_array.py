'''
Created on Jan 19, 2018

@author: qiankunhuang
'''
import heapq
def kth_array(a):
    sum=0
    for i in a:
        sum += len(i)
    res = []
    b= []
    for list in a:
        heapq.heappush(b,(list[0],0,list))
    while sum>0:
        c = heapq.heappop(b)
        res.append(c[0])
        if c[1]+1>=len(c[2]):
            sum-=1
        else:
            heapq.heappush(b,(c[2][c[1]+1],c[1]+1,c[2]))
            sum-=1
    return res
matrix=[[1,  3,   5,  7],[2,  4,   8, 9],[3,  5, 11, 15],[6,  8, 13, 18]]
print kth_array(matrix)   

            
            
     
    
     
    