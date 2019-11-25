##Given a binary tree, determine if it is a valid binary search tree (BST).
##Assume a BST is defined as follows:
##The left subtree of a node contains only nodes with keys less than the node's key.
##The right subtree of a node contains only nodes with keys greater than the node's key.
##Both the left and right subtrees must also be binary search trees.
##Example 1:
##    2
##   / \
##  1   3
##Input: [2,1,3]
##Output: true
##Example 2:
##    5
##   / \
##  1   4
##     / \
##    3   6
##Input: [5,1,4,null,null,3,6]
##Output: false
##Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        return


def isValidBST(root):
    if not root:
        return True
    min_node = -float("inf")
    max_node = float("inf")
    return isValidBST_help(root, min_node, max_node)


def isValidBST_help(node, min_node, max_node):
    if node is None:
        return True
    if node.val <= min_node or node.val >= max_node:
        return False
    return isValidBST_help(node.left, min_node, node.val) and isValidBST_help(node.right, node.val, max_node)
