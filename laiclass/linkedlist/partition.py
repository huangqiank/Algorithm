'''
Created on Jan 17, 2018

@author: qiankunhuang

'''


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, target):
        """
        head: ListNode
        target: int
        return: ListNode
        """
        small = Node(None)
        small_dummy = small
        large = Node(None)
        large_dummy = large
        dummy = head
        while dummy != None:
            if dummy.val <= target:
                small.next = Node(dummy.val)
                small = small.next
                dummy = dummy.next
            else:
                large.next = Node(dummy.val)
                large = large.next
                dummy = dummy.next
        small.next = large_dummy.next
        return small_dummy.next


node1 = Node(3)
node2 = Node(5)
node3 = Node(1)
node4 = Node(2)
node5 = Node(None)
node1.next = node2
node2.next = node3
node3.next = node4
###3512

def prit(node):
    while node != None:
        print(node.val)
        node = node.next


print(prit(Solution().partition(node1, 1)))
