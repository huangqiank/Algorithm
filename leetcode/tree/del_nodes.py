# 给出二叉树的根节点
# root，树上每个节点都有一个不同的值。
# 如果节点值在
# to_delete
# 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
# 返回森林中的每棵树。你可以按任意顺序组织答案。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


##           1
##         2   3
##       4  5 6  7
# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]
class Solution:
    def delNodes(self, root, to_delete):
        self.res = []
        rtest = self.trace(root, to_delete)
        if rtest != None:
            self.res.insert(0, root)
        return self.res
        # return [root, root.left]

    # 返回root为根节点，如果root.val in to_delete中，return None ,否则返回root
    def trace(self, root, to_delete):
        if root == None:
            return None
        t1 = self.trace(root.left, to_delete)
        t2 = self.trace(root.right, to_delete)
        root.left, root.right = t1, t2
        if root.val in to_delete:
            # root = None
            if t1 != None:
                self.res.append(t1)
            if t2 != None:
                self.res.append(t2)
            return None
        else:
            return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node
##        1
##      2   3
##     4 5 6 7
#3
s = Solution()
tmp = s.delNodes(node1,[3,5])
for i in tmp:
    print(i.val)
#print(tmp[0].val)
#print(tmp[1].val)
#print(tmp[2].val)
