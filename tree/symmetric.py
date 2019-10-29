'''
Created on Sep 9, 2017

@author: qiankunhuang
'''


class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order(self):
        res = []
        self.helper(self, res)
        return res

    def helper(self, res):
        if not self:
            return
        res.append(self.value)
        self.helper(self.left, res)
        self.helper(self.right, res)


def length(node):
    if not node:
        return 0
    a = length(node.left)
    b = length(node.right)
    return 1 + max(a, b)


def symmetric(node):
    if not node:
        return True
    return helper(node.left, node.right)


def helper(a, b):
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    if a.value != b.value:
        return False
    return helper(a.left, b.right) and helper(a.right, b.left)


node1 = Treenode(0)
node2 = Treenode(2)
node3 = Treenode(2)
node4 = Treenode(3)
node5 = Treenode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5

print(symmetric(node1))
