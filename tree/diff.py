class treenode:
    def __init__(self , x):
        self.left = None
        self.right =None
        self.val = x

def diffe(node1):
    dif =-2
    diff(node1,dif)
    return dif
dif =-2
def diff(node1):
    global dif
    if node1 is None:
        return 0
    left = diff(node1.left)
    right =diff(node1.right)
    dif = max(abs(left - right),dif)
    return [1 + max(left , right),dif]

node1 = treenode(3)
node2 = treenode(2)
node3 = treenode(4)         
node4 = treenode(-1)
node5 = treenode(3)
node6 = treenode(0)
node1.left = node2
node1.right = node3
node2.left= node4
node4.left = node6

print  diff(node1)   

