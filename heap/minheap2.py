'''
Created on Sep 10, 2017

@author: qiankunhuang
'''


##每层左右之间大小不用比较，最小堆：自上而下，上层最小
class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self, x):
        self.arr.append(x)
        self.size += 1
        self.percolate_up(self.size - 1)

    def percolate_up(self, index):
        while index > 0:
            parent = int((index - 1) / 2)
            if self.arr[parent] <= self.arr[index]:
                return
            else:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent

    def pop(self):
        a = self.arr[0]
        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
        self.size -= 1
        self.arr.remove(self.arr[self.size])  ###???
        self.percolate_down(0)
        return a

    def percolate_down(self, index):
        while index < self.size:
            lchild = 2 * index + 1
            rchild = 2 * index + 2
            if lchild > self.size - 1 and rchild > self.size - 1:
                return
            if rchild > self.size - 1:
                if self.arr[lchild] < self.arr[index]:
                    self.arr[lchild], self.arr[index] = self.arr[index], self.arr[lchild]
                    index = lchild
                else:
                    return
            if lchild <= self.size - 1 and rchild <= self.size - 1:
                if self.arr[index] <= self.arr[lchild] and self.arr[index] <= self.arr[rchild]:
                    return
                else:
                    if self.arr[lchild] < self.arr[rchild]:
                        self.arr[index], self.arr[lchild] = self.arr[lchild], self.arr[index]
                        index = lchild
                    else:
                        self.arr[index], self.arr[rchild] = self.arr[rchild], self.arr[index]
                        index = rchild


A = MinHeap()
A.arr = [1, 2, 3, 4]
A.size = 4
A.push(10)
print(A.arr)
A.push(-1)
print(A.arr)
A.push(1.5)
print(A.arr)
A.pop()
print(A.arr)
A.pop()
print(A.arr)
A.pop()
print(A.arr)

[1, 2, 3, 4, 10]
[-1, 2, 1, 4, 10, 3]
[-1, 2, 1, 4, 10, 3, 1.5]
[1, 2, 1.5, 4, 10, 3]
[1.5, 2, 3, 4, 10]
[2, 4, 3, 10]
