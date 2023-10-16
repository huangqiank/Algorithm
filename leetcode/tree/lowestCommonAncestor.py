##236. 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
##示例 1：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q):
        if root is None:
            return
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right


##1644. 二叉树的最近公共祖先 II
# 给定一棵二叉树的根节点 root，返回给定节点 p 和 q 的最近公共祖先（LCA）节点。
# 如果 p 或 q 之一 不存在 于该二叉树中，返回 null。树中的每个节点值都是互不相同的。
##根据维基百科中对最近公共祖先节点的定义：
# “两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是 后代节点 中既包括 p 又包括 q 的最深节点
# （我们允许 一个节点为自身的一个后代节点 ）”。一个节点 x 的 后代节点 是节点 x 到某一叶节点间的路径中的节点 y。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q):
        self.ans = None
        self.dfs(root, p, q)
        return self.ans

    ## all in one side
    ## in both side

    def dfs(self, root, p, q):
        if root is None:
            return False
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        flag = False
        if root == p or root == q:
            flag = True
            if left or right:
                self.ans = root
        if left and right :
            self.ans = root
        print(root.val,flag,left,right)
        return flag or left or right


node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(6)
node4 = TreeNode(2)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(1)
node8 = TreeNode(0)
node9 = TreeNode(8)
node1.left = node2
node2.left = node3
node2.right = node4
node4.left = node5
node4.right = node6
node1.right = node7
node7.left = node8
node7.right = node9

s = Solution1()
s.lowestCommonAncestor(node2, node2, node3)
