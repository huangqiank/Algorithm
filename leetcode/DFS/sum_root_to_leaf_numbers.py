##Given a binary tree containing digits from 0-9 only,
# each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
# Note: A leaf is a node with no children.
# Example:
# Input: [1,2,3]
#    1
#   / \
#  2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
# Input: [4,9,0,5,1]
#    4
#   / \
#  9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        if not root:
            return 0
        stack = [(root, root.val)]
        res = []
        while stack:
            n = len(stack)
            for i in range(n):
                root, total = stack.pop(0)
                if not root.left and not root.right:
                    res.append(total)
                if root.left:
                    stack.append((root.left, 10 * total + root.left.val))
                if root.right:
                    stack.append((root.right, 10 * total + root.right.val))
        return sum(res)

    def sumNumbers2(self, root):
        if not root:
            return
        self.res = 0


        def helper(root, tmp):
            if not root:
                return
            if not root.left and not root.right:
                self.res += tmp
                return
            if root.left:
                helper(root.left, 10 * tmp + root.left.val)
            if root.right:
                helper(root.right, 10 * tmp + root.right.val)
        helper(root, root.val)
        return self.res
