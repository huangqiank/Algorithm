'''
Created on Sep 10, 2017

@author: qiankunhuang
'''
##插入，enqueue先进后出

class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, x):
        node = Node(x)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return
        else:
            a = self.head
            self.head = self.head.next
        self.size -= 1
        return a


def findMiddle(llist):
    curQuickNode = llist.head
    curSlowNode = llist.head
    while curQuickNode != None:
        if curQuickNode.next is None:
            return curSlowNode.value
        curQuickNode = curQuickNode.next.next
        curSlowNode = curSlowNode.next
    return curSlowNode.value


node1 = Node(0)
node2 = Node(2)
node3 = Node(4)

node1.next = node2
node2.next = node3

q1 = Queue()
q1.tail = node3
q1.head = node1

print(findMiddle(q1))

   
    