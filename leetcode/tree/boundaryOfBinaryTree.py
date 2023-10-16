##545 二叉树的 边界 是由 根节点 、左边界 、按从左到右顺序的 叶节点 和 逆序的右边界 ，按顺序依次连接组成。
#左边界 是满足下述定义的节点集合：
#根节点的左子节点在左边界中。如果根节点不含左子节点，那么左边界就为 空 。
#如果一个节点在左边界中，并且该节点有左子节点，那么它的左子节点也在左边界中。
#如果一个节点在左边界中，并且该节点 不含 左子节点，那么它的右子节点就在左边界中。
#最左侧的叶节点 不在 左边界中。
#右边界 定义方式与 左边界 相同，只是将左替换成右。即，右边界是根节点右子树的右侧部分；叶节点 不是 右边界的组成部分；如果根节点不含右子节点，那么右边界为 空 。
#叶节点 是没有任何子节点的节点。对于此问题，根节点 不是 叶节点。
#给你一棵二叉树的根节点 root ，按顺序返回组成二叉树 边界 的这些值。
#示例 1：
#输入：root = [1,null,2,3,4]
#输出：[1,3,4,2]
#解释：
#- 左边界为空，因为二叉树不含左子节点。
#- 右边界是 [2] 。从根节点的右子节点开始的路径为 2 -> 4 ，但 4 是叶节点，所以右边界只有 2 。
#- 叶节点从左到右是 [3,4] 。
#按题目要求依序连接得到结果 [1] + [] + [3,4] + [2] = [1,3,4,2] 。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        self.buttom = []
        self.left = []
        self.right = []
        if root.left is None and root.right is None:
            return [root.val]
        self.buttom_bundary(root)
        self.left_boundary(root.left)
        self.right_boundary(root.right)
        res = [root.val] + self.left + self.buttom + self.right[::-1]
        return res

    def buttom_bundary(self, root):
        if root and root.left is None and root.right is None:
            self.buttom.append(root.val)
        if root.left:
            self.buttom_bundary(root.left)
        if root.right:
            self.buttom_bundary(root.right)

    def left_boundary(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        self.left.append(root.val)
        if root.left:
            self.left_boundary(root.left)
        else:
            self.left_boundary(root.right)

    def right_boundary(self, root):
        if root is None or (root.left is None and root.right is None):
            return
        self.right.append(root.val)
        if root.right:
            self.right_boundary(root.right)
        else:
            self.right_boundary(root.left)










class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root.left is None and root.right is None:
            return [root.val]
        self.left = []
        self.buttom = []
        self.right = []
        self.leftOfBinaryTree(root.left)
        self.buttomOfBinaryTree(root)
        self.rightOfBinaryTree(root.right)
        res = [root.val] + self.left + self.buttom + self.right[::-1]
        return res

    def leftOfBinaryTree(self, root):
        if root and (root.left != None or root.right != None):
            self.left.append(root.val)
            if root.left:
                self.leftOfBinaryTree(root.left)
            else:
                self.leftOfBinaryTree(root.right)

    def rightOfBinaryTree(self, root):
        if root and (root.left != None or root.right != None):
            self.right.append(root.val)
            if root.right:
                self.rightOfBinaryTree(root.right)
            else:
                self.rightOfBinaryTree(root.left)

    def buttomOfBinaryTree(self, root):
        if root and root.left is None and root.right is None:
            self.buttom.append(root.val)
        if root.left:
            self.buttomOfBinaryTree(root.left)
        if root.right:
            self.buttomOfBinaryTree(root.right)


