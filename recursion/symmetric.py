'''
Created on Sep 23, 2017

@author: qiankunhuang
'''
def symmetric(node):
    if node is None:
        return True
    symmetric_help(node.left,node.right)

def symmetric_help(node1,node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    return symmetric_help(node1.left,node2.right) and symmetric_help(node1.right,node2.left)

