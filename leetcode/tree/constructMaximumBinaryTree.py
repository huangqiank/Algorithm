##654. 最大二叉树
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
# 返回 nums 构建的 最大二叉树 。
# 示例 1：
# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
#    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
#        - 空数组，无子节点。
#        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
#            - 空数组，无子节点。
#            - 只有一个元素，所以子节点是一个值为 1 的节点。
#    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
#        - 只有一个元素，所以子节点是一个值为 0 的节点。
#        - 空数组，无子节点。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]):

        n = len(nums)
        return self.constructBinaryTree(nums, 0, n )

    def constructBinaryTree(self, nums, left, right):
        if left >= right:
            return None
        tmp = (-float("inf"), 0)
        for i in range(left, right):
            if nums[i] > tmp[0]:
                tmp = (nums[i], i)
        node = TreeNode(tmp[0])
        node.left = self.constructBinaryTree(nums, left, tmp[1])
        node.right = self.constructBinaryTree(nums, tmp[1] + 1, right)
        return node
