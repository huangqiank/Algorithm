'''
Created on Sep 10, 2017

@author: qiankunhuang
'''

import operator


class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class Stack(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a


Global = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


def revPoland(alist):
    numStack = Stack()
    for x in alist:
        if x not in Global:
            numStack.push(x)
        else:
            right = numStack.pop()
            left = numStack.pop()
            numStack.push(Global[x](left, right))
    return numStack.pop()


print(revPoland([1, 2, 3, "+", "-"]))

        
        
###重做