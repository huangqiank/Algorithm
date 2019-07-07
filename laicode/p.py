'''
Created on Jan 20, 2018

@author: qiankunhuang
'''
import heapq
def find_k(a,k):
    dict = {}
    for i in a:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
    b =[]
    res=[]
    for i in dict.keys():
        heapq.heappush(b,[-dict[i],i])
    while k>0:
        k-=1
        c= heapq.heappop(b)
        res.append(c[1])
    return res
A="aaaabbbcccccdef"
print (find_k(A,2))     
    
def kth_matrix(a,k):
    heap=[]
    n = len(a)
    res=[]
    for i in range(n):
        heapq.heappush(heap,(a[i][0],0,a[i]))
    while k > 1 :
        k-=1
        c = heapq.heappop(heap)
        if c[1] < len(c[2])-1:
            heapq.heappush(heap,(c[2][c[1]+1],c[1]+1,c[2]))
    c = heapq.heappop(heap)
    res.append(c[0])
    return res
matrix=[[1,  3,   5,  7],[2,  4,   8, 9],[3,  5, 11, 15],[6,  8, 13, 18]]
print kth_matrix(matrix,5)            


def merge_k_array(a):
    res=[]
    n = len(a)
    d=[]
    for list in a:
        heapq.heappush(res,(list[0],0,list))
    while len(res) != 0:
        c=heapq.heappop(res)
        d.append(c[0])
        if c[1]+1 <len(c[2]):
            heapq.heappush(res,(c[2][c[1]+1],c[1]+1,c[2]))
    return d
matrix=[[1,  3,   5,  7],[2,  4,   8, 9],[3,  5, 11, 15],[6,  8, 13, 18]]
print merge_k_array(matrix)   

a=[1,2,3,4]
a=1
print a+1 
a=[1,2,3,4]
print min(a)
            
            
        
    
            
        
        
        
 