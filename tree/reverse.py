'''
Created on Sep 16, 2017

@author: qiankunhuang
'''
class Treenode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    def pre_order(self,root):
        res=[]
        self.helper(res,root)
        return res
    def helper(self,res,root):
        if not root:
            return 
        res.append(root.value)
        self.helper(res,root.left,)
        self.helper(res,root.right)
                

            

def invert_tree(root):
    if not root:
        return
    root.left ,root.right= root.right , root.left
    invert_tree(root.left)
    invert_tree(root.right)

node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(4)
node4 = Treenode(-1)
node5 = Treenode(1)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4


invert_tree(node1)
print (node1.right.right.val)

