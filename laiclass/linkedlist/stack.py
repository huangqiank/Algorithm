'''
Created on Sep 9, 2017

@author: qiankunhuang
'''


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        else:
            a = self.top.value
            self.top = self.top.next
        self.size -= 1
        return a

##先进先出
class Queue:
    def __int__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def deQueue(self):
        if not self:
            return
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a

    def enqueue(self, value):
        node = Node(value)
        if not self:
            return
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


node1 = Node(0)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node1.next = node2
node2.next = node3
q = Stack()
q.top = node1
q.push(5)
print(q.pop())
print(q.top.value)