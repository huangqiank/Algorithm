class Treenode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


def print_same_level(node):
    res = []
    queue = [node]
    while queue:
        n = len(queue)
        this_level = []
        while n > 0:
            n -= 1
            node = queue.pop(0)
            this_level.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        res.extend(this_level)
    return res


node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(4)
node4 = Treenode(-1)
node5 = Treenode(3)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node6
node3.left = node5
##        3
##      2   4
##    -1     3
##   0

print(print_same_level(node1))
