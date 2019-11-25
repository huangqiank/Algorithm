##Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
##For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
##    1
##   / \
##  2   2
## / \ / \
##3  4 4  3
##But the following [1,2,2,null,3,null,3] is not:
##    1
##   / \
##  2   2
##   \   \
##   3    3
##Note:
##Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetric_help(root.left, root.right)

    def isSymmetric_help(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.isSymmetric(node1.left, node2.right) and self.isSymmetric(node1.right, node2.left)
