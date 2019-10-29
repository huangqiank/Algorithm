class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def TreeNodeCnt(node):
    if not node:
        return 0
    left = TreeNodeCnt(node.left)
    right = TreeNodeCnt(node.right)
    return 1 + left + right


treenode1 = TreeNode(10)
treenode1.left = TreeNode(5)
treenode1.right = TreeNode(15)
treenode1.left.left = TreeNode(2)
treenode1.left.right = TreeNode(7)
treenode1.left.left.left = TreeNode(1)
treenode1.right.left = TreeNode(12)
treenode1.right.right = TreeNode(20)

print(TreeNodeCnt(treenode1))
print(TreeNodeCnt(treenode1.left))
print(TreeNodeCnt(treenode1.left.left))
print(TreeNodeCnt(treenode1.left.left.left))
##
