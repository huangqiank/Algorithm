'''
Created on Feb 18, 2018

@author: qiankunhuang
'''


class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def getsum(root):
    if not root:
        return 0
    res = [0]
    sumhelp(root, res, 0)
    return res[0]


def sumhelp(root, res, cur):
    if not root:
        return
    cur = cur * 10 + root.value
    if not root.left and not root.right:
        res[0] += cur
        print(res)
    sumhelp(root.left, res, cur)
    sumhelp(root.right, res, cur)




node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(5)
node4 = Treenode(-1)
node5 = Treenode(3)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
print(getsum(node1))
