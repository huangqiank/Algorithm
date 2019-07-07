'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
class listnode:
    def __init__(self,value):        
        self.next = None
        self.value = value
class queue:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None
    def enqueue(self,value):
        node=listnode(value)
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
        

node1 = listnode(0)
node2 = listnode(1)
node3 = listnode(2)
node4 = listnode(3)
node1.next = node2
node2.next = node3
q=queue()
q.tail = node1
q.head = node3
q.enqueue(5)
print q.dequeue()
print q.tail.value

                     
        
        
        
    