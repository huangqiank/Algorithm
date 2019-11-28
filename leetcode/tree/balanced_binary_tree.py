# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node
# differ in height by no more than 1.
# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#    3
#   / \
#  9  20
#    /  \
#   15   7
# Return true.
# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
# Return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isBalanced(self, root):
        return self.getHeight(root) != -1

    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) >= 2:
            return -1
        return 1 + max(left,right)
