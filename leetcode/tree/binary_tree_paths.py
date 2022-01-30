# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。

# 示例:

# 输入:

#   1
# /   \
# 2     3
# \
#  5


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        self.res = []
        self.dfs(root, str(root.val))
        return self.res

    def dfs(self, root, combination):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.res.append(combination)
        if root.left != None:
            self.dfs(root.left, combination + "->" + str(root.left.val))
        if root.right != None:
            self.dfs(root.right, combination + "->" + str(root.right.val))


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
a.left = b
a.right = c
b.right = d
s = Solution()
print(s.binaryTreePaths(a))
