'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def pre_order(self):
        res=[]
        self.helper(self,res)
        return res
    def helper(self,res):
        if not self:
            return 
        res.append(self.value)
        self.helper(self.left,res)
        self.helper(self.right,res)
                
def length(node):
    if not node:
        return 0     
    a = length(node.left)
    b = length(node.right)
    return 1+max(a,b)


    
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
print (length(node1) )
        
      


    
    
     