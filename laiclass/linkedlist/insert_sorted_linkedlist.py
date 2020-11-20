'''
Created on Jan 17, 2018

@author: qiankunhuang
'''


class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution(object):
    def insert(self, head, value):
        node = Node(value)
        dummy = head
        if dummy is None:
            node.next = dummy
            return node
        while dummy != None:
            if dummy.value <= node.value and (dummy.next is None or dummy.next.value >= node.value):
                node.next = dummy.next
                dummy.next = node
                return head
            elif dummy.value > node.value:
                node.next = dummy
                return node
            elif dummy.next.value <= node.value:
                dummy = dummy.next


node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)
node5 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4


def prit(node):
    while node != None:
        print(node.value)
        node = node.next


print(prit(Solution().insert(node1, 8)))


## a b c d
## a b e c d
## 1. 如果大于所有的 ， 则在最后面
## 2。 如果大于 当前， 小于 后一个， 则插入