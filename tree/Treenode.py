class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def length(node):
    if node is None:
        return 0
    a = length(node.left)
    b = length(node.right)
    return 1 + max(a, b)


'''
bbt树的高度查小于1，平衡二叉树
'''


def bbt(node):
    if node is None:
        return True
    if abs(length(node.left) - length(node.right)) > 1:
        return False
    else:
        return bbt(node.left) and bbt(node.right)


def balanced2(node):
    if node is None:
        return True
    left = balanced2(node.left)
    right = balanced2(node.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)


'''
自己的值大于左子,小于右子，binary search tree
'''


def bst(root):
    min = -2 * float("inf")
    max = 2 * float("inf")
    return compare(root, min, max)


def compare(root, min, max):
    if not root:
        return True
    if root.value < min or root.value > max:
        return False
    return compare(root.left, min, root.value) and compare(root.right, root.value, max)

class Solution(object):
    def inOrder(self,root):
        res = []
        if root is None:
            return res
        self.help(res,root)
        return res

    def help(self,res,root):
        if root is None:
            return
        self.help(res,root.left)
        res.append(root.value)
        self.help(res,root.right)


T1 = TreeNode(0)
T2 = TreeNode(1)
T3 = TreeNode(2)
T4 = TreeNode(3)
T1.left = T2
T2.left = T3
T3.right = T4

print(Solution().inOrder(T1))












node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(-1)
node5 = TreeNode(3)
node6 = TreeNode(0)
#        3
###    2    5
###  -1
##      3


node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node5
#print(balanced2(node1))
print(bst(node1))
