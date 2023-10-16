##314. 二叉树的垂直遍历
#给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。
#如果两个结点在同一行和列，那么顺序则为 从左到右。
#示例 1：
#输入：root = [3,9,20,null,null,15,7]
#输出：[[9],[3,15],[20],[7]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##dfs      F
import collections
class Solution:
    def verticalOrder(self, root):
        self.dict= collections.defaultdict(list)
        x,y=0,0
        self.inorder(x,y,root)
        res=[]
        for x in sorted(list(self.dict.keys())):
            level=[]
            for j in sorted(self.dict[x], key=lambda t:t[0]):
                level.append(j[1])
            res.append(level)
        return res

    def inorder(self,x,y,root):
        if not root:
            return
        self.dict[x].append((y,root.val))
        self.inorder(x-1,y+1,root.left)
        self.inorder(x+1,y+1,root.right)

class Solution2:
    def verticalOrder2(self, root):
        x_dict= collections.defaultdict(list)
        x,y=0,0
        queue= [(x,root)]
        res=[]
        while queue:
            n= len(queue)
            while n>0:
                x,node = queue.pop(0)
                x_dict[x].append((y,node.val))
                n-=1
                if node.left:
                    queue.append((x-1,node.left))
                if node.right:
                    queue.append((x+1,node.right))
            y+=1
        for x in sorted(list(x_dict.keys())):
            level=[]
            for j in sorted(x_dict[x], key=lambda t:t[0]):
                level.append(j[1])
            res.append(level)
        return res

