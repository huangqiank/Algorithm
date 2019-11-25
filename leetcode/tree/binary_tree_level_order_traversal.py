##Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
##For example:
##Given binary tree [3,9,20,null,null,15,7],
##    3
##   / \
##  9  20
##    /  \
##   15   7
##return its level order traversal as:
##[
##  [3],
##  [9,20],
##  [15,7]
##]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return
        all_res = []
        cur_res = [[root]]
        while cur_res:
            tmp = []
            this_level = []
            cur = cur_res.pop(0)
            for node in cur:
                this_level.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if len(tmp) > 0:
                cur_res.append(tmp)
            all_res.append(this_level)
        return all_res


def levelOrder(root):
    all_res = []
    cur_res = [[root]]
    while cur_res:
        tmp = []
        this_level = []
        cur = cur_res.pop(0)
        for node in cur:
            this_level.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        if len(tmp)>0:
            cur_res.append(tmp)
        all_res.append(this_level)
    return all_res

###      3
##     2    4
##   -1   3
##  0
node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(4)
node4 = TreeNode(-1)
node5 = TreeNode(3)
node6 = TreeNode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node6
node3.left = node5
print(levelOrder(node1))
