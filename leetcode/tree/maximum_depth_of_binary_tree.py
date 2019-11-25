##Given a binary tree, find its maximum depth.
##The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
##Note: A leaf is a node with no children.
##Example:
##Given binary tree [3,9,20,null,null,15,7],
##    3
##   / \
##  9  20
##    /  \--09
##   15   7
##return its depth = 3.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node2.left = node3
node3.right= node4
node2.right = node5
print(maxDepth(node1))