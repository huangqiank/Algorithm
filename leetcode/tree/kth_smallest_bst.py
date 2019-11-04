# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        rank = 0
        res = []
        while root or res:
            if root:
                res.append(root)
                root = root.left
            else:
                root = res.pop()
                rank +=1
                if rank == k :
                    return root.val
                root = root.right
        return



