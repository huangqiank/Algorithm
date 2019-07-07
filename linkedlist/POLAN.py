'''
Created on Sep 10, 2017

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
import operator
Global_Operator = {"+": operator.add ,"-":operator.sub,"*": operator.mul ,"/":operator.div}
def rev_polish(alist):
    num_stack = stack()
    for x in alist:
        if x not in Global_Operator:
            num_stack.push(x)
        else:
            right = num_stack.pop()
            left = num_stack.pop()
            num_stack.push(Global_Operator[x](left,right))
    return num_stack.pop()
            
print rev_polish([1,2,3,"+","-"])
        
        
###重做