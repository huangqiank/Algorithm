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


def helper(root, k1, k2):
    if not root:
        return
    if root.value > k1 and root.value < k2:
        print(root.value)
        helper(root.left, k1, k2)
        helper(root.right, k1, k2)
    if root.value > k2:
        helper(root.left, k1, k2)
    if root.value < k1:
        helper(root.right, k1, k2)


node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(4)
node4 = Treenode(-1)
node5 = Treenode(3)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

##          3
##       2     4
##    -1   3  0
##
helper(node1, -1000, 1000)
