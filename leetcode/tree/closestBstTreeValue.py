# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        res = root.val
        while root:
            if root.val ==target:
                return root.val
            if abs(root.val - target) < abs(root.val - target):
                res = root.val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return res
