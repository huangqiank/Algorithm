#Given a complete binary tree, count the number of nodes.
#Note:
#Definition of a complete binary tree from Wikipedia:
#In a complete binary tree every level,
# except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#计算树
#相等，则左满右不一定
#不相等，左不一定，右满
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        a = self.countNodes(root.left)
        b = self.countNodes(root.right)
        return 1 + a + b
    def countNodes2(self,root):
        if not root:
            return 0
        left= self.get_height(root.left)
        right =self.get_height(root.right)
        if left == right:
            return 2**left + self.countNodes2(root.right)
        return 2**right + self.countNodes2(root.left)


    def get_height(self,root):
        if not root:
            return 0
        a = self.get_height(root.left)
        b = self.get_height(root.right)
        return 1+ max(a,b)




