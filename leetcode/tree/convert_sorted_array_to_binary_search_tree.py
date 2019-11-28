##Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
##For this problem, a height-balanced binary tree is defined as a binary tree
##in which the depth of the two subtrees of every node never differ by more than 1.
##Example:
##Given the sorted array: [-10,-3,0,5,9],
##One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
##      0
##     / \
##   -3   9
##   /   /
## -10  5

##inorder : [val : index]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

##包括左边界不包括右边界
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        return self.sortedArrayToBST_help(nums, 0, len(nums))

    def sortedArrayToBST_help(self, nums, left, right):
        if left >= right:
            return None
        mid = int((left + right) / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST_help(nums, left, mid )
        root.right = self.sortedArrayToBST_help(nums, mid + 1, right)
        return root




