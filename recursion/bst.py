'''
Created on Sep 23, 2017

@author: qiankunhuang
'''


class Treenode:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
def bst(node):
    if node is None:
        return 0
    left = bst(node.left)
    right = bst(node.right)
    if left == -1 or right == -1:
        return -1
    if  abs(left-right) > 1:
        return -1
    return 1 + max(left,right)
node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(5)
node4 = Treenode(-1)
node5 = Treenode(1)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
print bst(node1)

