##Given a linked list, rotate the list to the right by k places,
##where k is non-negative.

##Example 1:

##Input: 1->2->3->4->5->NULL, k = 3
##Output: 4->5->1->2->3->NULL
##Explanation:
##rotate 1 steps to the right: 5->1->2->3->4->NULL
##rotate 2 steps to the right: 4->5->1->2->3->NULL
##Example 2:
##Input: 0->1->2->NULL, k = 4
##Output: 2->0->1->NULL
##Explanation:
##rotate 1 steps to the right: 2->0->1->NULL
##rotate 2 steps to the right: 1->2->0->NULL
##rotate 3 steps to the right: 0->1->2->NULL
##rotate 4 steps to the right: 2->0->1->NULL


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotateRight(head, k):
    if not head:
        return head
    tmp = head
    l = 0
    while tmp:
        tmp = tmp.next
        l += 1
    k = k % l
    if k == 0:
        return head
    pre_head = head
    quick_head = head
    for i in range(k):
        quick_head = quick_head.next
    while quick_head.next:
        quick_head = quick_head.next
        pre_head = pre_head.next
    tmp = pre_head.next
    quick_head.next = head
    pre_head.next = None
    return tmp


def prit(head):
    while head:
        print(head.val)
        head = head.next


node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)

node1.next = node2
node2.next = node3

k = 4
prit(rotateRight(node1, k))
