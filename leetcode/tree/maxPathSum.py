##124. 二叉树中的最大路径和
# 路径 被定义为一条从树中任意节点出发，
# 沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中 至多出现一次 。
# 该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
# 示例 1：
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        self.maxSum =  -float("inf")
        self.maxGain(root)
        return self.maxSum

    def maxGain(self, root):
        if root is None:
            return 0
        left = max(self.maxGain(root.left),0)
        right = max(self.maxGain(root.right),0)
        maxGain = root.val + left + right
        self.maxSum = max(self.maxSum,maxGain)
        return root.val + max(left,right)
