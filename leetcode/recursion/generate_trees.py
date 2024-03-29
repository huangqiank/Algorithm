# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

# 示例：
# 输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#  1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int):
        if not n:
            return []
        return self.help(1, n)

    def help(self, start, end):
        res = []
        if start > end:
            return [None]
        for i in range(start, end + 1):
            left_nodes = self.help(start, i - 1)
            right_nodes = self.help(i + 1, end)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    res.append(node)
        return res