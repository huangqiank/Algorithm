##623. Add One Row to Tree
#Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
#Note that the root node is at depth 1.
#The adding rule is:
#Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
#cur's original left subtree should be the left subtree of the new left subtree root.
#cur's original right subtree should be the right subtree of the new right subtree root.
#If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
#Example 1:
#Input: root = [4,2,6,3,1,5], val = 1, depth = 2
#Output: [4,1,1,2,null,null,6,3,1,5]

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth ==1:
            new = TreeNode(val)
            new.left = root
            return new
        if not root:
            return
        root.left =self.dfs(root.left,val,depth-1,0)
        root.right = self.dfs(root.right,val,depth-1,1)
        return root
    def dfs(self,node,val,depth,flag):
        if depth == 1:
            new = TreeNode(val)
            if flag == 0:
                new.left = node
            else:
                new.right = node
            return new
        if not node:
            return
        node.left = self.dfs(node.left,val,depth-1,0)
        node.right = self.dfs(node.right, val, depth - 1, 1)
        return node
