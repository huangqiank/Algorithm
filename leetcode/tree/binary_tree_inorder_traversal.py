##Given a binary tree, return the inorder traversal of its nodes' values.
##Example:
##Input: [1,null,2,3]
##   1
##    \
##     2
##    /
##   3
##Output: [1,3,2]
##Follow up: Recursive solution is trivial, could you do it iteratively?
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


##先左再中再右
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.help(root, res)

    def help(self, root, res):
        if root is None:
            return
        self.help(root, root.left)
        res.append(root.val)
        self.help(root, root.right)


def inorder(root):
    white, black = 0, 1
    res = []
    if not root:
        return
    node_stack = [(white, root)]
    while node_stack:
        color, node = node_stack.pop()
        if node:
            if color == white:
                node_stack.append((white, node.right))
                node_stack.append((black, node))
                node_stack.append((white, node.left))
            else:
                res.append(node.val)
    return res


node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(-1)
node5 = TreeNode(3)
node6 = TreeNode(0)

node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
#        3
#    2       5
# -1
#     3
##-1,3,2,3,5
print(inorder(node1))


##         3, 3  3
##-1
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.help(root, res)

    def help(self, root, res):
        if root is None:
            return
        self.help(root, root.left)
        res.append(root.val)
        self.help(root, root.right)


##  left,mid,right
def inorder1(self, root):
    res = []
    stack = []
    res.append(root)
    while root != None or len(stack) != 0:
        if root != None:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
            stack.append(root)


##  mid left right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.help(root)
        return self.res

    def help(self, root):
        if root is None:
            return
        self.res.append(root.val)
        if root.left:
            self.help(root.left)
        if root.right:
            self.help(root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while root != None or len(stack) != 0:
            while root != None:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res


##left right mid
class Solution:
    def postorderTraversal(self, root):
        self.res = []
        self.help(root)
        return self.res

    def help(self, root):
        if root is None:
            return
        if root.left:
            self.help(root.left)
        if root.right:
            self.help(root.right)
        self.res.append(root.val)


## left right mid
## mid right left , two linklist
class solution:
    def postorderTraversal(self, root):
        res = []
        stack = []
        while root != None or len(stack) != 0:
            while root != None:
                res.append(root.val)
                stack.append(root)
                root = root.right
            root = stack.pop()
            root = root.left
        tmp = res[::-1]
        return tmp


## one list
## add : 1. leaf node  2. has already visited left and right
## left right mid
class solution2:
    def postorderTraversal(self, root):
        res = []
        stack = []
        pre = None
        while root != None or len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left
            if len(stack) != 0:
                root = stack.pop()
                if root.right != None and root.right != pre:
                    ## don't visited this root
                    stack.append(root)
                    root = root.right
                else:
                    res.append(root.val)
                    pre = root
                    root = None
        return res


## left right mid

class solution3:
    def postorderTraversal(self, root):
        stack = []
        res = []
        pre = None
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                if root.right != None and root.right != pre:
                    stack.append(root)
                    root = root.right
                else:
                    res.append(root)
                    pre = root
                    root = None
        return res

    ##     1
    ##  2     3
    ##4   5  6  7
    ## 1245367
    ##mid left right
    def preorder(self, root):
        stack = []
        res = []
        while root or len(stack) != 0:
            while root:
                res.append(root)
                stack.append(root)
                root = root.left
            if len(stack) > 0:
                root = stack.pop()
                root = root.right
        return res



    ##4251637
    ##left mid right
    def inorder(self, root):
        stack = []
        res = []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            if len(stack)>0:
                root = stack.pop()
                res.append(root)
                root = root.right
        return res

