#250. 统计同值子树
#给定一个二叉树，统计该二叉树数值相同的子树个数。
#同值子树是指该子树的所有节点都拥有相同的数值。
#示例：
#输入: root = [5,1,5,5,5,null,5]
#              5
#             / \
#            1   5
#           / \   \
#          5   5   5
#输出: 4
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1240:
    def countUnivalSubtrees(self, root):
        self.count = 0
        if root is None:
            return self.count
        self.help(root)
        return self.count

    def help(self, root):
        if root is None:
            return True
        tmp1 = self.help(root.left)
        tmp2 = self.help(root.right)
        if tmp1 !=True or tmp2 !=True:
            return False
        if root.left != None and root.right != None:
            if root.val == root.left.val and root.val == root.right.val:
                self.count += 1
                return True
            else:
                return False
        elif root.left != None:
            if root.val == root.left.val:
                self.count += 1
                return True
            else:
                return False
        elif root.right != None:
            if root.val == root.right.val:
                self.count += 1
                return True
            else:
                return False
        else:
            self.count += 1
            return True

