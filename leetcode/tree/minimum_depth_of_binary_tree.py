##The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        child = [root.left, root.right]
        if not any(child):
            return 1
        min_length = float("inf")
        for c in child:
            if c:
                min_length = min(min_length, self.minDepth(c))
        return 1 + min_length


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.right = node4
node3.left = node5
s = Solution()
print(s.minDepth(node1))


##DFS
class Solution2:
    def minDepth2(self, root):
        if not root:
            return 0
        stack = [(1, root)]
        min_length = float("inf")
        while stack:
            height, node = stack.pop()
            child = [node.left, node.right]
            if not any(child):
                min_length = min(min_length, height)
            for c in child:
                if c:
                    stack.append((height + 1, c))
        return min_length


##BFS
class Solution3:
    def minDepth3(self, root):
        if not root:
            return 0
        stack = [(1, root)]
        while stack:
            height, node = stack.pop(0)
            child = [node.left, node.right]
            if not any(child):
                return height
            for c in child:
                if c:
                    stack.append((height + 1, c))
