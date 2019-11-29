##Given a singly linked list, determine if it is a palindrome.
##Example 1:
# Input: 1->2
##Output: false
##Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## tmp.next = None 则 return head ==tmp.next
## 反转链表
##中间值

class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        prepare = None
        pre =head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
            pre.next = prepare
            prepare = pre
        if fast != None:
            slow = slow.next
        while pre != None and slow != None:
            if pre.val != slow.val:
                return False
            pre = pre.next
            slow = slow.next
        return True

        ##0->1->2
        ##0<-1->2
        ##0<-1-<2
