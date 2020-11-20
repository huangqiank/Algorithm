'''
Created on Sep 18, 2017

@author: qiankunhuang
'''


class Listnode:
    def __init__(self, x):
        self.next = None
        self.val = x


### ab cd
### ba dc
def reverse_pair(node):
    if node is None or node.next is None:
        return node
    next_next = node.next
    new = reverse_pair(node.next.next)
    node.next = new  ## a--->d
    next_next.next = node  ## b--->a
    return next_next

def reverse_pair2(node):
    if node is None or node.next is None:
        return node
    next_node = node.next
    new = reverse_pair2(node.next.next)
    node.next.next = node
    node.next = new
    return next_node

# 1234
# 2143


def prit(node):
    while node != None:
        print(node.val)
        node = node.next


A = Listnode(1)
B = Listnode(2)
C = Listnode(3)
D = Listnode(4)
E = Listnode(5)
A.next = B
B.next = C
C.next = D
D.next = E
##1234
##21435
reverse_pair2(A)
prit(B)



