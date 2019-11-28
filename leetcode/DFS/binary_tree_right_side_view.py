# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# Example:
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#   1            <---
# /   \
# 2     3         <---
# \     \
#  5     4       <---


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if i == n - 1:
                    res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res
