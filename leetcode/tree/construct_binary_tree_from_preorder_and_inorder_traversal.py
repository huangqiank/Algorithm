##Given preorder and inorder traversal of a tree, construct the binary tree.
##Note:
##You may assume that duplicates do not exist in the tree.
##For example, given
##preorder = [3,9,20,15,7]
##先中再左再右、
##inorder = [9,3,15,20,7]
##先左再中再右
##Return the following binary tree:
##    3
##   / \
##  9  20
##    /  \
##   15   7

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: key for key, val in enumerate(inorder)}
        self.buildTreehelp(inorder_map, preorder, 0, len(preorder), inorder, 0, len(inorder))

    def buildTreehelp(self, inorder_map, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start == pre_end:
            return None
        root_value = preorder[pre_start]
        root = TreeNode(root_value)
        index = inorder_map[root_value]
        left_num = index - in_start
        root.left = self.buildTreehelp(inorder_map, preorder, pre_start + 1, pre_start + 1 + left_num, inorder,
                                       in_start, index)
        root.right = self.buildTreehelp(inorder_map, preorder, pre_start + 1 + left_num, pre_end, inorder,
                                        index + 1, in_end)
        return root
