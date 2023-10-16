# 426. 将二叉搜索树转化为排序的双向链表
# 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。
# 对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，
# 第一个节点的前驱是最后一个节点，
# 最后一个节点的后继是第一个节点。
# 特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，
# 树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


###        1
##     -1      2
###  -2   0  1.5   5
## -2 -1 0 1 1.5 2 5
## inorder
##left mid right
class Solution:
    def treeToDoublyList(self, root):
        if root is None:
            return
        self.first = None
        self.last = None
        self.pre_order(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first

    def pre_order(self, root):
        if root is None:
            return
        self.pre_order(root.left)
        if self.first is None:
            self.first = root
        else:
            self.last.right = root
            root.left = self.last
        self.last = root
        self.pre_order(root.right)
        return root

##left mid right
class Solution:
    def treeToDoublyList(self, root):
        if root is None:
            return
        self.last = None
        self.first = None
        self.inorder(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.first is None:
            self.first = root
        if self.last != None:
            self.last.right = root
            root.left = self.last
        self.last = root
        self.inorder(root.right)

