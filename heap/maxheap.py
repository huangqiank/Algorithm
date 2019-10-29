'''
Created on Sep 11, 2017

@author: qiankunhuang
'''
class MaxHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push_max(self,val):
        self.arr.append(val)
        self.size += 1
        index = self.size
        self.percolate_up_max(index-1)
    

    def percolate_up_max(self,index):
        while index > 0 :
            parent =int((index-1)/2)
            if self.arr[parent]  <  self.arr[index]:
                self.arr[parent] , self.arr[index] = self.arr[index] , self.arr[parent]
                index = parent  
            else:
                return  

        
    def pop_max(self):
        self.size  -= 1
        a = self.arr[0]
        self.arr[0] , self.arr[self.size] = self.arr[self.size] , self.arr[0]
        self.arr.remove(self.arr[self.size])      
        self.percolate_down_max(0)
        return a



   
    def percolate_down_max(self,index):    
        while index  < self.size:
                lchild = 2*index + 1
                rchild = 2*index + 2 
                if lchild > self.size - 1 and rchild > self.size - 1:
                    return 
                if rchild > self.size - 1:
                    if self.arr[lchild] > self.arr[index]:
                        self.arr[lchild] , self.arr[index] = self.arr[index] , self.arr[lchild]
                        index = lchild
                    else:
                        return
                if lchild <= self.size - 1 and rchild <= self.size - 1:
                    if self.arr[index] >= self.arr[lchild] and self.arr[index] >= self.arr[rchild]:
                        return
                    else:
                        if self.arr[lchild] < self.arr[rchild]:
                            self.arr[index] , self.arr[rchild] = self.arr[rchild] , self.arr[index]
                            index = rchild
                        else:
                            self.arr[index] , self.arr[lchild] = self.arr[lchild] , self.arr[index]
                            index = lchild

                
                
A=MaxHeap()
A.arr=[5,4,3,2,1,-1]
A.size=6
A.push_max(-2)
print(A.arr)
A.push_max(10)
print(A.arr)
A.push_max(4.5)
print(A.arr)
A.pop_max()
print(A.arr)
A.pop_max()
print (A.arr)
           
                          
        
   
        
        