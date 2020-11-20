'''
Created on Dec 12, 2017

@author: qiankunhuang
'''
class heap:
    def __init__(self):
        self.size =0
        self.arr=[]
    def push(self,value):
        self.arr.append(value)
        self.size += 1
        self.perculate_up(self.size-1)

    def pop(self):
        self.size -= 1
        self.arr[0] ,self.arr[self.size] = self.arr[self.size] , self.arr[0]
        self.arr.pop()
        self.perculate_down(0)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    def perculate_up(self,index):
        while index > 0 :
            parent = (index -1)/2
            if self.arr[index] < self.arr[parent]:
                self.arr[parent] , self.arr[index] = self.arr[index] , self.arr[parent]
                index = parent
            else:
                return
    def perculate_down(self,index):
        while index + 1 < self.size:
            lchild = 2*index + 1
            rchild = 2*index + 2
            if lchild > self.size - 1:
                return
            if rchild > self.size - 1:
                if self.arr[lchild] > self.arr[index]:
                    return
                else:
                    self.arr[lchild] , self.arr[index] = self.arr[index] , self.arr[lchild]
                    index = lchild
            else:
                if self.arr[lchild] < self.arr[rchild]:
                    min = lchild
                else:
                    min = rchild
                if self.arr[min] < self.arr[index]:
                    self.arr[min] , self.arr[index] = self.arr[index] , self.arr[min]
                    index = min
                else:
                    return
import heapq
def kth_largest(a,k):
    b = a[:k]
    heapq.heapify(b)
    for i in range(k,len(a),1):
        if a[i] > b[0]:
            heapq.heappop(b)
            heapq.heappush(b,a[i])
        else:
            continue
    return b[0]



           
                   
    
        
        
    
        
                    
                    
                    
                
             
                
                    
                    
                    
            
            
                
            
        
            
            
            
            
            
            
        
        
                                                                    
        
        