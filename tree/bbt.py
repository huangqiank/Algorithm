'''
Created on Sep 9, 2017

@author: qiankunhuang
'''


class TreeNode:
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
    if node is None:
        return 0
    a = length(node.left)
    b = length(node.right)
    return 1 + max(a, b)


def balanced(node):
    if not node:
        return True
    if abs(length(node.left) - length(node.right)) > 1:
        return False
    else:
        return balanced(node.left) and balanced(node.right)


def bbt(node):
    if node is None:
        return 0
    left = bbt(node.left)
    right = bbt(node.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)


node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(-1)
node5 = TreeNode(1)
node6 = TreeNode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
print(balanced(node1))
print(bbt(node1))
