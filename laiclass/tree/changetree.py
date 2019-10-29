'''
Created on Sep 11, 2017

@author: qiankunhuang
'''
class Treenode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def change_subtree(root):
    if not root:
        return 0
    left = change_subtree(root.left)
    right = change_subtree(root.right)
    root.val = left
    return 1 + left + right



treenode1 = Treenode(10)
treenode1.left = Treenode(5)
treenode1.right = Treenode(15)
treenode1.left.left = Treenode(2)
treenode1.left.right = Treenode(7)
treenode1.left.left.left = Treenode(1)
treenode1.right.left = Treenode(12)
treenode1.right.right = Treenode(20)

print (change_subtree(treenode1))
print (change_subtree(treenode1.left))
print (change_subtree(treenode1.left.left))
print (change_subtree(treenode1.left.left.left))
##
