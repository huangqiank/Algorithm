'''
Created on Sep 21, 2017

@author: qiankunhuang
'''
class Node:
    def __init__(self , x):
        self.left = None
        self.right = None
        self.val = x
        
def print_by_level(root):
    if not root:
        return []
    result = []
    queue=[root]
    while queue:
        num = len(queue)
        this_level = []
        for i in xrange(0,num):
            node = queue[0] 
            this_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            del queue[0]
        result.append(this_level)
    return result
  
root = Node(0)
root.left = Node(1)
root.left.left = Node(2)
root.left.right = Node(3)

def print_by_level1(node):
    res = []
    queue=[node]
    while queue:
        n = len(queue)
        this_level=[]
        for i in xrange(0 , n  ,1):
            a = queue.pop(0)
            this_level.append(a.val)
            if a.left != None:
                queue.append(a.left)
            if a.right != None:
                queue.append(a.right)
        res.append(this_level)
    return res
                
print print_by_level1(root)            
            