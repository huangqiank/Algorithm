'''
Created on Sep 18, 2017

@author: qiankunhuang
'''


class Treenode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x


def get_height(node):
    if node is None:
        return 0
    left = get_height(node.left)
    right = get_height(node.right)
    return 1 + max(left, right)


node1 = Treenode(0)
node2 = Treenode(1)
node3 = Treenode(1)
node4 = Treenode(2)
node5 = Treenode(2)
node6 = Treenode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
print(get_height(node1))
