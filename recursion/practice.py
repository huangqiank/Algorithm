'''
Created on Sep 25, 2017

@author: qiankunhuang
'''
class Node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x
        
class resultwrapper:
    def __init__(self):
        self.global_max = -1
        self.solution = None
def find_max(node):
    res = resultwrapper()
    find_max_difference(node,res)
    print res.solution.val
     
def find_max_difference(node,res):
    if node is None:
        return 0
    left = find_max_difference(node.left,res)
    right = find_max_difference(node.right,res)
    if abs(left-right) > res.global_max:
        res.global_max = abs(left-right)
        res.solution = node
    return 1 + left+right

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node1.left = node2
node1.right = node3
node1.left.left = node4
node1.left.left.left = node5
node1.left.left.right = node6

  
find_max(node1)




    
    


        
        
        
        
        
    