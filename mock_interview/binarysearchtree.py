'''
Created on Oct 21, 2017

@author: qiankunhuang
'''
def binarysearchtree(node):
    if node is None:
        return True
    k1="-inf"
    k2="inf"
    return binarysearch_help(node,k1,k2)
def binarysearch_help(node,k1,k2):
    if node is None:
        return True
    if k1 >= node.val or k2 <= node.val:
        return False
    return binarysearch_help(node.left,k1,node.val) and binarysearch_help(node.right,node.left,k2)
        