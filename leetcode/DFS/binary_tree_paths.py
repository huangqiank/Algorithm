##Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.
##Example:
##Input:
##   1
## /   \
##2     3
## \
##  5
##Output: ["1->2->5", "1->3"]

##Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return ""
        self.res = []
        tmp = str(root.val)

        def binaryTreePaths_help(root, tmp):
            if not root.left and not root.right:
                return self.res.append(tmp)
            if root.left:
                binaryTreePaths_help(root.left, tmp + "->" + str(root.left.val))
            if root.right:
                binaryTreePaths_help(root.right, tmp + "->" + str(root.right.val))

        binaryTreePaths_help(root, tmp)
        return self.res
