'''
Created on Sep 21, 2017

@author: qiankunhuang
'''
class Node:
    def __init__(self , x):
        self.left = None
        self.right = None
        self.value = x

def printSameLevel(node):
    res= []
    queue = [node]
    while queue:
        n = len(queue)
        thisLevel = []
        while n > 0 :
            n-=1
            a = queue.pop(0)
            thisLevel.append(a.value)
            if a.left != None:
                queue.append(a.left)
            if a.right != None:
                queue.append(a.right)
        print(thisLevel)
        res.extend(thisLevel)
    return res


root = Node(0)
root.left = Node(1)
root.left.left = Node(2)
root.left.right = Node(3)
print (printSameLevel(root) )
            