'''
Created on Sep 10, 2017

@author: qiankunhuang
'''
class Listnode:
    def __init__(self,value):        
        self.next = None
        self.value = value
class Queue:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None
    def enqueue(self,value):
        node=Listnode(value)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size +=1
    def dequeue(self):
        if self.size is None:
            return False
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a
    def value(self):
        return self.value

def find_middle(llist):
    cur_quick_tail = llist.tail
    cur_slow_tail = llist.tail
    while cur_quick_tail != None:
        if cur_quick_tail.next is None:
            return cur_slow_tail.value
        cur_quick_tail = cur_quick_tail.next.next        
        cur_slow_tail = cur_slow_tail.next
    return cur_slow_tail.value  
        
node1 = Listnode(0)
node2 = Listnode(2)
node3 = Listnode(4)

node1.next = node2
node2.next = node3

q1=Queue()
q1.tail = node1
q1.head = node3

   
   
print find_middle(q1)
   
    