##814. 二叉树剪枝
##给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。
##返回移除了所有不包含 1 的子树的原二叉树。
##节点 node 的子树为 node 本身加上所有 node 的后代。
##示例 1：
##输入：root = [1,null,0,0,1]
##输出：[1,null,0,null,1]
##解释：
##只有红色节点满足条件“所有不包含 1 的子树”。 右图为返回的答案
# 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.check(root):
            return None
        return root
    def check(self,root):
        if root is None:
            return True
        left = self.check(root.left)
        right = self.check(root.right)
        if left:
            root.left = None
        if right :
            root.right = None
        if left and right and root.val == 0:
            return True
        return False
