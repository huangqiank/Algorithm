'''
Created on Sep 10, 2017

@author: qiankunhuang
'''
class MinHeap:
    def __init__(self):
        self.size = 0
        self.arr = []
   
    def push(self,value):
        self.arr.append(value)
        self.size += 1
        self.percolate_up(self.size-1)
        
    def percolate_up(self,index):
        while index > 1:
            parent_index = (index-1)/2
            if self.arr[index] < self.arr[parent_index]:
                self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
                index = parent_index   
    def pop(self):
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self.percolate_down(0)
    
    def percolate_down(self,index):
        while index  < self.size /2:
            childl = 2*index + 1
            childr = 2*index + 2

A= MinHeap()
A.arr=[1,2,3,4]
A.size=4
A.push(10)
print A.arr
A.push(-1)
print A.arr
A.push(1.5)
print A.arr
A.pop()
print A.arr
A.pop()
print A.arr
A.pop()
print A.arr

            