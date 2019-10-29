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


def bst(root):
    min = -2 * float("inf")
    max = 2 * float("inf")
    return helper(root, min, max)


def helper(root, min, max):
    if not root:
        return True
    if root.value < min or root.value > max:
        return False
    return helper(root.left, min, root.value) and helper(root.right, root.value, max)


node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(5)
node4 = Treenode(-1)
node5 = Treenode(3)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
print(bst(node1))
