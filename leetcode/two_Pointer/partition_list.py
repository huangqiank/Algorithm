##Given a linked list and a value x,
##partition it such that all nodes less than x
##come before nodes greater than or equal to x.

##You should preserve the original relative order of the nodes
##in each of the two partitions.

##Example:
##Input: head = 1->4->3->2->5->2, x = 3
##Output: 1->2->2->4->3->5

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head, x):
    if not head:
        return head
    tmp1 = ListNode(0)
    small = tmp1
    tmp2 = ListNode(0)
    large = tmp2
    new = head
    while new:
        if new.val < x:
            small.next = new
            small = small.next
        else:
            large.next = new
            large = large.next
        new=new.next
    large.next = None
    small.next = tmp2.next
    return tmp1.next

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next =node2
node2.next =node3
node3.next =node4
node4.next =node5
node5.next =node6
k =3


def prit(head):
    while head:
        print(head.val)
        head = head.next
prit(partition(node1,k))