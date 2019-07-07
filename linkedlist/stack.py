'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
class listnode:
    def __init__(self,value):        
        self.next = None
        self.value = value
class stack:
    def __init__(self):
        self.size = 0
        self.tail = None
    def push(self,value):
        node=listnode(value)
        if self.tail == None:
            self.tail = node
        else:
            node.next = self.tail
            self.tail = node
        self.size +=1
    def pop(self):
        if self.size == 0:
            return False
        else:
            a = self.tail.value
            self.tail= self.tail.next
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
q=stack()
q.tail = node1
q.push(5)
print q.pop()
print q.tail.value
                 
        
        
        
    