##Given a binary tree
##struct Node {
##  int val;
##  Node *left;
##  Node *right;
##  Node *next;
##}
##Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
##Initially, all next pointers are set to NULL.
##Example:
##Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
##Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
##Explanation: Given the above binary tree (Figure A),
# your function should populate each next pointer to point to its next right node,
# just like in Figure B.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root):
        if not root:
            return root
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect2(self, root):
        if not root:
            return root
        stack = [[root]]
        while stack:
            this_level = stack.pop(0)
            tmp = []
            for i in range(len(this_level) - 1):
                this_level[i].next = this_level[i + 1]
            for node in this_level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if len(tmp) > 0:
                stack.append(tmp)
        return root
