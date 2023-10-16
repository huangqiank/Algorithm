##1171. Remove Zero Sum Consecutive Nodes from Linked List
# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.
# (Note that in the examples below, all sequences are serializations of ListNode objects.)
# Example 1:
# Input: head = [1,2,-3,3,1]
# Output: [3,1]
# Note: The answer [1,2,1] would also be accepted.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head):
        sum_node = {}
        pre = ListNode()
        pre.next = head
        dummy = pre
        total = 0
        while dummy:
            total += dummy.val
            sum_node[total] = dummy
            dummy = dummy.next
        dummy = pre
        total = 0
        while dummy:
            total += dummy.val
            dummy.next = sum_node[total].next
            dummy = dummy.next
        return pre.next


##


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head):
        pre = ListNode()
        pre.next = head
        dummy = pre
        sum_node = {}
        total = 0
        while dummy:
            total += dummy.val
            sum_node[total] = dummy
            dummy = dummy.next
        dummy = pre
        total = 0
        ## if total is 0 , next point won't be 0
        while dummy:
            total += dummy.val
            dummy.next = sum_node[total].next
            dummy = dummy.next
        return pre.next
