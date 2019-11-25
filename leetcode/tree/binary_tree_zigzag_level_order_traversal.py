##Given a binary tree, return the zigzag level order traversal of its nodes
##values. (ie, from left to right, then right to left for the next level and alternate between).

##For example:
##Given binary tree [3,9,20,null,null,15,7],
##    3
##   / \
##  9  20
##    /  \
##   15   7
##return its zigzag level order traversal as:
##[
##  [3],
##  [20,9],
##  [15,7]
##]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        return 0


def zigzagLevelOrder(root):
    flag = 1
    queue = [[root]]
    res = []
    while queue:
        cur = queue.pop(0)
        this_level = []
        tmp = []
        for node in cur:
            this_level.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        if len(tmp) > 0:
            queue.append(tmp)
        if flag == 1:
            res.append(this_level)
            flag = -1
        else:
            this_level.reverse()
            res.append(this_level)
            flag = 1
    return res
