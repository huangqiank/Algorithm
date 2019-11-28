# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted linked list: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5],
# which represents the following height balanced BST:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        self.sortedListToBST_help(head, None)

    def sortedListToBST_help(self, head, end):
        if head == end:
            return None
        mid = self.find_mid(head, end)
        mid_node = TreeNode(mid.val)
        mid_node.left = self.sortedListToBST_help(head, mid)
        mid_node.right = self.sortedListToBST_help(mid.next, end)
        return mid_node

    def find_mid(self, head, end):
        if not head:
            return
        fast = head
        slow = head
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        return slow

class Solution:

    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head.
        if prevPtr:
            prevPtr.next = None

        return slowPtr


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

