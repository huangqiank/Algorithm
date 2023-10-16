##Given a linked list, remove the n-th node from the end of list
##and return its head.
##Example:
##Given linked list: 1->2->3->4->5, and n = 2.
##After removing the second node from the end,
##the linked list becomes 1->2->3->5.
##Note:
##Given n will always be valid.
##Follow up:
##Could you do this in one pass?
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    j = 0
    slow_head = ListNode(0)
    fast_head = ListNode(0)
    slow_head.next = head
    fast_head.next = head
    i = 0
    while fast_head.next:
        if j < n:
            j += 1
            fast_head = fast_head.next
        else:
            i += 1
            fast_head = fast_head.next
            slow_head = slow_head.next
    slow_head.next = slow_head.next.next
    if i == 0:
        return head.next
    else:
        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast_head = head
        slow_head = head
        while n > 0:
            fast_head = fast_head.next
            n-=1
        if fast_head is None:
            return head.next
        while fast_head.next :
            slow_head = slow_head.next
            fast_head= fast_head.next
        slow_head.next = slow_head.next.next
        return head



def prit(head):
    while head:
        print(head.val)
        head = head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
prit(removeNthFromEnd(node1, 2))
