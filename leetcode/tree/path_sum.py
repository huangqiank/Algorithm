##Given a binary tree and a sum, determine if the tree has a root-to-leaf path
##such that adding up all the values along the path equals the given sum.
##Note: A leaf is a node with no children.
##Example:
##Given the below binary tree and sum = 22,
##      5
##     / \
##    4   8
##   /   / \
##  11  13  4
## /  \      \
##7    2      1
##return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        total = 0
        if not root:
            return False
        return self.hasPathSum_help(total, root, sum)

    def hasPathSum_help(self, total, root, sum):
        total += root.val
        if not root.left and not root.right:
            if total == sum:
                return True
            return False
        if root.left and root.right:
            return self.hasPathSum_help(total, root.left, sum) or self.hasPathSum_help(total, root.right, sum)
        if root.left:
            return self.hasPathSum_help(total, root.left, sum)
        if root.right:
            return self.hasPathSum_help(total, root.right, sum)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        self.targetSum = targetSum
        total = root.val
        return self.dfs(root,total)
    def dfs(self,root,total):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if total == self.targetSum:
                return True
            return False
        left = False
        right = False
        if root.left:
            left = self.dfs(root.left, total+ root.left.val)
        if root.right:
            right = self.dfs(root.right, total+ root.right.val)
        return left or right

node1 = TreeNode(1)
s = Solution()
print(s.hasPathSum(node1, 1))
