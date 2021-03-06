class treenode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


dif = -2


def diffe(node1):
    diff(node1)
    return dif


def diff(node1):
    global dif
    if node1 is None:
        return 0
    left = diff(node1.left)
    right = diff(node1.right)
    dif = max(abs(left - right), dif)
    return 1 + max(left, right)


node1 = treenode(3)
node2 = treenode(2)
node3 = treenode(4)
node4 = treenode(-1)
node5 = treenode(3)
node6 = treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node6


##         3
##       2    4
##    -1
##   0


def diff(node):
    dif = 0
    dif_help(dif, node)
    return dif


def dif_help(dif, node):
    if node is None:
        return  0
    left = diff(dif.left, node)
    right = diff(dif.right, node)
    dif = max(left - right, dif)
    return 1 + max(left, right)


print(diffe(node1))
