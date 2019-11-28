##Given a binary tree, flatten it to a linked list in-place.
##For example, given the following tree:
##    1
##   / \
##  2   5
## / \   \
##3   4   6
##The flattened tree should look like:

##1
## \
##  2
##  \
##    3
##     \
##      4
##       \
##        5
##         \
##          6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

##后序遍历，先左再右再中
##找到左边的起点：pre_start
##找到左边的终点：pre_end
##pre_end 指到根节点的右边
##根节点的左边清空
##一次遍历


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            pre_start = root.left
            while pre_start.right:
                pre_start = pre_start.right
            pre_start.right = root.right
            root.right = root.left
            root.left = None
