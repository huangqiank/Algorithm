# 给定一个 N 叉树，返回其节点值的 后序遍历 。
# N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
# 进阶：#递归法很简单，你可以使用迭代法完成此题吗?


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


## 左右中

class Solution:
    def postorder(self, root):
        s = []
        res = []
        while len(s) != 0 and root != None:
            while root != None:
                s.append(root)
                root = root.left
            node = s.pop()
            res.append(node)
            root = node.right
        return res


## 左中右 iteration 写法
##
class Solution1:
    def inorder(self, root):
        s = []
        res = []
        while len(s) != 0 or root != None:
            while root != None:
                s.append(root)
                root = root.left
            node = s.pop()
            res.append(node)
            root = node.right
        return res


## 中左右
class Solution:
    def preorderTraversal(self, root):
        res = list()
        if not root:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res


## 左右中
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return list()
        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ## 在右边有值的时候需要继续遍历, 直到遍历完再回溯，且 非第二次遍历
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


##              1
##          2      3
##        4   5  6   7

## 124
## pop 4  pre= 4, root = None
## 1  pop 2 pre = 4
## 1 pop5


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[5,6,3,2,4,1]
## 左右中
class Solution:
    def postorder(self, root):
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return
        for child in root.children:
            self.dfs(child)
        self.res.append(root.val)

#左右中
## 把这一层压进去，
class Solution:
    def postorder(self, root):
        self.res = []
        self.dfs(root)
        return self.res


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


## 中左右
class Solution:
    def preorder(self, root: 'Node'):
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return
        self.res.append(root.val)
        for node in root.children:
            self.dfs(node)

## 中左右
class Solution:
    def preorder(self, root: 'Node'):
        s = [root]
        res = []
        while len(s) != 0:
            tmp = s.pop()
            res.append(tmp)
            s.extend(root.children[::-1])
        return res




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
        self.stack=[]
        self.iter(root)
    def iter(self,root):
        if root is None:
            return
        while root:
            self.stack.append(root)
            root =root.left
    def next(self):
        tmp =self.stack.pop()
        if tmp.right != None:
            self.iter(tmp.right)
        return tmp.val
    def hasNext(self) -> bool:
        if len(self.stack) != 0 :
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()