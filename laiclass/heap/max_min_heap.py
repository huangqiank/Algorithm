'''
Created on Jan 21, 2018

@author: qiankunhuang
'''
import heapq
class max_heap_int(object):
    def __init__(self,val):
        self.val =val
    def __it__(self,other):
        return self.val >other.val
    def __eq__(self,other):
        return self.val == other.val
    def __str__(self):
        return self(self.val)
    def onine_median(self,input):
        min_heap = []
        max_heap=[]
        res=[]
        for i in range(len(input)):
            if not min_heap:
                heapq.heappush(min_heap,input[i])
            else:
                if input[i] >= min_heap[0]:
                    heapq.heappush(min_heap,input[i])
                else:
                    heapq.heappush(max_heap,input[i])
            if len(min_heap) >len(max_heap)+1:
                    heapq.heappush(max_heap,max_heap_int(min_heap[0]))
                    heapq.heappop(min_heap)
            elif len(max_heap)> len(min_heap):
                    heapq.heappush(min_heap,max_heap[0].val)
                    heapq.heappop(max_heap)
            if len(min_heap) == len(max_heap):
                res.append(0.5(min_heap[0]+max_heap[0].val))
            else:
                res.append(min_heap[0])
        return res
                    
                
        
                    
                    