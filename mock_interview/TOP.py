'''
Created on Nov 5, 2017

@author: qiankunhuang
'''
import heapq
def top_k(s,k):
    dict={}
    res=[]
    for i in s:
        if  i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict.keys():
        heapq.heappush(res,(dict[i],i))
        if len(res) >= k:
            heapq.heappop(res)
    res2=[]
    for j in xrange(len(res)):
        res2.append(heapq.heappop(res)[1])
    return res2
            
            