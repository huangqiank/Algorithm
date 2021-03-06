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
        
def parathesis(b): 
    a = stack()   
    for i in b:
        if i in["(","[","{"]:
            a.push(i)
        if i == ")":
            if a.size == 0 or a.pop() != "(":
                return False           
        if i == "]":
            if a.size == 0 or a.pop() != "[":
                return False               
        if i == "}":
            if a.size == 0 or a.pop() != "{":
                return False 
    if a.size != 0:
        return False
    else:
        return True

b=["(","[","{","}","]",")"]
print (parathesis(b))
c=["(","]",")"]
print (parathesis(c))


