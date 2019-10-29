class Treenode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

##是不是共同的节点
def LCA(start, n1, n2):
    if start is None:
        return None
    if start == n1 or start == n2:
        return start
    left = LCA(start.left, n1, n2)
    right = LCA(start.right, n1, n2)
    if left and right:
        return start
    if left:
        return left
    if right:
        return right


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

##      3
##    2   5
##  -1
##    3
##

print(LCA(node1,node5,node3).val)
