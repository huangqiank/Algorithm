##109. 有序链表转换二叉搜索树
##给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
##本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
##示例:
##给定的有序链表： [-10, -3, 0, 5, 9],
##一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#      0
#     / \
#   -3   9
#   /   /
# -10  5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        return self.build_tree(head, None)

    def build_tree(self, left, right):
        if left == right:
            return None
        mid = self.find_mid(left, right)
        mid_node = TreeNode(mid.val)
        mid_node.left = self.build_tree(left, mid)
        mid_node.right = self.build_tree(mid.next, right)
        return mid_node

    ##1234
    ##3
    ##       3
    ##      2  4
    ##     1
    def find_mid(self, left, right):
        slow, fast = left, left
        while fast != right and fast.next != right:
            fast = fast.next.next
            slow = slow.next
        return slow

