'''
Created on Sep 17, 2017

@author: qiankunhuang
'''

class Listnode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def reverse_linklist(node):
    if node is None or node.next is None:
        return node
    newend = reverse_linklist(node.next)
    node.next.next = node
    node.next = None
    return newend
A=Listnode(1)
B=Listnode(2)      
C=Listnode(3)     
D=Listnode(4)  
A.next = B
B.next = C   
C.next = D
reverse_linklist(A)
print D.next.val
print C.next.val
print B.next.val

