##1120. 子树的最大平均值
##给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。
##子树是树中的任意节点和它的所有后代构成的集合。
##树的平均值是树中节点值的总和除以节点数。
##示例：
##输入：[5,6,1]
##输出：6.00000
##解释：
##以 value = 5 的节点作为子树的根节点，得到的平均值为 (5 + 6 + 1) / 3 = 4。
##以 value = 6 的节点作为子树的根节点，得到的平均值为 6 / 1 = 6。
##以 value = 1 的节点作为子树的根节点，得到的平均值为 1 / 1 = 1。
##所以答案取最大值 6。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maximumAverageSubtree(self, root) -> float:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return 0, 0
        lc, ls = self.dfs(root.left)
        rc, rs = self.dfs(root.right)
        self.res = max(self.res, (root.val + ls + rs) / (1 + lc + rc))
        return 1 + lc + rc, root.val + ls + rs


class Treenode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


s = Solution()
node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(5)
node4 = Treenode(-1)
node5 = Treenode(3)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
print(s.maximumAverageSubtree(node1))

# 3
##     2      5
##   -1
##        3
