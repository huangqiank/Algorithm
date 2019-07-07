'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
class ListNode:
    def __init__(self,value):        
        self.next = None
        self.value = value

def reverse(node):
    if node.next == None:
        return node
    newend = reverse(node.next)
    node.next.next=node
    node.next=None
    return newend

def reverse2(node):
    if node is None or node.next is None:
        return node    
    next_node = node.next    
    new_end = reverse2(node.next)   
    next_node.next=node
    node.next = None 
    return new_end   
A=ListNode(1)
B=ListNode(2)      
C=ListNode(3)     
D=ListNode(4)  
A.next = B
B.next = C   
C.next = D
reverse2(A)     



