##Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).

##For example:
##Given binary tree [3,9,20,null,null,15,7],
##    3
##   / \
##  9  20
##    /  \
##   15   7
##return its bottom-up level order traversal as:
##[
##  [15,7],
##  [9,20],
##  [3]
##]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return
        res = []
        queue = [[root]]
        self.levelOrderBottom_help(queue, res)

    def levelOrderBottom_help(self, queue, res):
        while queue:
            this_Level = []
            cur = queue.pop(0)
            tmp =[]
            for node in cur:
                this_Level.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if len(tmp) > 0:
                queue.append(tmp)
            res.append(this_Level)
        res.reverse()
        return res
