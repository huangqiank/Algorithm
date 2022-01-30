##Given an integer n, generate all structurally unique BST's
##(binary search trees) that store values 1 ... n.
##Example:
##Input: 3
##Output:
##[
##  [1,null,3,2],
##  [3,2,null,1],
##  [3,1,null,null,2],
##  [2,1,3],
##  [1,null,2,null,3]
##]
##Explanation:
##The above output corresponds to the 5 unique BST's shown below:
##   1         3     3      2      1
##    \       /     /      / \      \
##     3     2     1      1   3      2
##    /     /       \                 \
##   2     1         2                 3
##左边小，右边大
# Definition for a binary tree node.

##写一个当前节点的函数，深层所有可能的当前层
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generateTrees(n):
    if not n:
        return []
    return generateTrees_help(1, n)


def generateTrees_help(start, end):
    res = []
    if start > end:
        return [None]
    for i in range(start, end + 1):
        left = generateTrees_help(start, i - 1)
        right = generateTrees_help(i + 1, end)
        for l in left:
            for r in right:
                cur = TreeNode(i)
                cur.left = l
                cur.right = r
                res.append(cur)
    return res
