'''
Created on Jan 17, 2018

@author: qiankunhuang
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inOrder(self, root):
        res = []
        if root is None:
            return res
        self.help(res, root)
        return res

    def help(self, res, root):
        if root is None:
            return
        self.help(res, root.left)
        res.append(root.val)
        self.help(res, root.right)


T1 = TreeNode(0)
T2 = TreeNode(1)
T3 = TreeNode(2)
T4 = TreeNode(3)
T1.left = T2
T2.left = T3
T3.right = T4
##中序遍历，左中右
##      0
##     1
##    2
##      3
print(Solution().inOrder(T1))
