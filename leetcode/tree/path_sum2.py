##Given a binary tree and a sum,
##find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.
##Example:
##Given the below binary tree and sum = 22,
##      5
##     / \
##    4   8
##   /   / \
##  11  13  4
## /  \    / \
##7    2  5   1
##Return:
##[
##   [5,4,11,2],
##   [5,8,4,5]
##]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        def pathSum_help(tmp, root, sum):
            if not root:
                return
            sum -= root.val
            ##不可以这么写
            ##            tmp += [root.val]
            if not root.left and not root.right:
                if sum == 0:
                    res.append(tmp)
                    return
            pathSum_help(tmp + [root.val], root.left, sum)
            pathSum_help(tmp + [root.val], root.right, sum)

        res = []
        if not root:
            return res
        pathSum_help([], root, sum)
        return res


class Solution2:
    def pathSum(self, root, sum):
        res = []
        if not root:
            return res
        self.pathSum_help([], root, sum, res)
        return res

    def pathSum_help(self, tmp, root, sum, res):
        if not root:
            return res
        sum -= root.val
        ##不可以这么写
        ##tmp += [root.val]
        if not root.left and not root.right:
            if sum == 0:
                tmp.append(root.val)
                res.append(tmp)
            return
        self.pathSum_help(tmp + [root.val], root.left, sum, res)
        self.pathSum_help(tmp + [root.val], root.right, sum, res)


class Solution3:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [([root.val], root)]
        while stack:
            tmp, node = stack.pop(0)
            if not node.left and not node.right and sum(tmp) == node.val:
                res.append(tmp)
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
        return res


s = Solution2()
a = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node8
node4.left = node7
node3.left = node5
node3.right = node6
node6.left = node9
node6.right = node10
t = 22
print(s.pathSum(node1, t))
