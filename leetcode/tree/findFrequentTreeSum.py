##508. 出现次数最多的子树元素和
#给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。
# 如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
#一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#示例 1：
#输入: root = [5,2,-3]
#输出: [2,-3,4]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.total_cnt= {}
        self.max_cnt = 0
        self.dfs(root)
        res=[]
        for num in self.total_cnt.keys():
            if self.total_cnt[num] == self.max_cnt:
                res.append(num)
        return res
    def dfs(self,root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        tmp = left + right + root.val
        self.total_cnt[tmp] =  self.total_cnt.get(tmp,0) +1
        self.max_cnt = max(self.max_cnt,self.total_cnt[tmp])
        return tmp

