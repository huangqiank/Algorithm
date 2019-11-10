# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s=[]
        cur = root
        rank = 0
        while cur or s:
            if cur:
                s.append(cur.val)
                cur = cur.left
            else:
                if k == rank:
                    return  s.pop()
                rank +=1
                s.append(cur.right)
                cur = cur.right



