##Given a linked list,
##return the node where the cycle begins. If there is no cycle,
##return null.
##To represent a cycle in the given linked list,
##we use an integer pos which represents the position (0-indexed) in the linked list
##where tail connects to. If pos is -1, then there is no cycle in the linked list.
##Note: Do not modify the linked list.
##Example 1:
##Input: head = [3,2,0,-4], pos = 1
##Output: tail connects to node index 1
##Explanation: There is a cycle in the linked list, where tail connects to the second node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    slow = head
    quick = head

    while True:
        if quick or quick.next or quick.next.next:
            return None
        slow = slow.next
        quick = quick.next.next
        if slow == quick:
            break
    new = head
    while slow:
        if slow == new:
            return new
        new = new.next
        slow = slow.next


node1 = ListNode(1)


print(detectCycle(node1))