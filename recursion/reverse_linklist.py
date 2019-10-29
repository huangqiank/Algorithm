'''
Created on Sep 17, 2017

@author: qiankunhuang
'''

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseLinkedList(node):
    if node is None or node.next is None:
        return node
    end = reverseLinkedList(node.next)
    node.next.next = node
    node.next = None
    return end

##1234
##2143
def reversePair(node):
    if node is None or node.next is None:
        return node
    next_next = node.next
    new = reversePair(node.next.next)
    node.next = new
    next_next.next = node
    return next_next

def prit(node):
    while node != None:
        print(node.val)
        node = node.next

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
A.next = B
B.next = C
C.next = D
reverseLinkedList(A)

