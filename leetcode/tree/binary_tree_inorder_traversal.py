##Given a binary tree, return the inorder traversal of its nodes' values.
##Example:
##Input: [1,null,2,3]
##   1
##    \
##     2
##    /
##   3
##Output: [1,3,2]
##Follow up: Recursive solution is trivial, could you do it iteratively?
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


##先左再中再右
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.help(root, res)

    def help(self, root, res):
        if root is None:
            return
        self.help(root, root.left)
        res.append(root.val)
        self.help(root, root.right)


def inorder(root):
    white, black = 0, 1
    res = []
    if not root:
        return
    node_stack = [(white, root)]
    while node_stack:
        color, node = node_stack.pop()
        if node:
            if color == white:
                node_stack.append((white, node.right))
                node_stack.append((black, node))
                node_stack.append((white, node.left))
            else:
                res.append(node.val)
    return res


node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(-1)
node5 = TreeNode(3)
node6 = TreeNode(0)

node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
#        3
#    2       5
# -1
#     3
##-1,3,2,3,5
print(inorder(node1))
