'''
Created on Sep 30, 2017

@author: qiankunhuang
'''
import heapq
def find_k2(A,k):
    B={}
    C=[]
    for i in A:
        if i not in B:
            B[i] = 1
        else:
            B[i] += 1
    for j in B:
        heapq.heappush(C,(B[j],j))
        if len(C) > k:
            heapq.heappop(C)
    return C
    top=[]
    for i in xrange(0,k):
        top.append(heapq.heappop(C)[1])
    top.reverse()
    return top
A="aaaabbbcccccdef"
print (find_k2(A,2))       
          
            
    

        