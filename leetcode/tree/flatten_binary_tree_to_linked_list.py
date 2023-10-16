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


## mid left right

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


#     0
#   4（pre）2
#  1  1
#      2
#       3
#
## 4--1--2--3--2


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []
        self.inorder(root)
        for i in range(0, len(self.res) - 1):
            self.res[i].left = None
            self.res[i].right = self.res[i + 1]

        return

    def inorder(self, root):
        if root is None:
            return
        self.res.append(root)
        self.inorder(root.left)
        self.inorder(root.right)


## mid  -> left -> right
## right <-left <- mid
class Solution1:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre = None
        self.postorder(root)
    def postorder(self,root):
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root


## mid -> left -> right
class Solution2:
    def flatten(self, root):
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


