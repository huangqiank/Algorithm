'''
Created on Sep 17, 2017

@author: qiankunhuang
'''
from collections import deque


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
#reverseLinkedList(A)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.mid(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        dummy = Node(0)
        tmp = dummy
        while l1 or l2:
            if l1 != None:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
            if l2 != None:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
        return tmp.next
    def mid(self,node):
        slow = node
        fast = node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow= slow.next
        return slow
    def reverse(self,node):
        if node is None or node.next is None:
            return node
        next = node.next
        tmp  = self.reverse(next)
        next.next = node
        node.next = None
        return tmp

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
A.next = B
B.next = C
C.next = D
D.next = E
s = Solution()
h = s.reorderList(A)

#[1 ]
##root = 2

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.dfs(head)
        return head

    def dfs(self, head):
        tmp = head
        last = None
        while tmp:
            nxt = tmp.next
            if tmp.child:
                last_child = self.dfs(tmp.child)
                nxt = tmp.next
                tmp.next = tmp.child
                tmp.child.prev = tmp
                if nxt:
                    last_child.next = nxt
                    nxt.prev = last_child
                tmp.child = None
                last = last_child
            else:
                last = tmp
            tmp = nxt
        return last



a = deque([1,2,3])
print(a.pop())
