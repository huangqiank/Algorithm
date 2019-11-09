##Sort a linked list in O(n log n) time using constant space complexity.
##Example 1:
##Input: 4->2->1->3
##Output: 1->2->3->4
##Example 2:
##Input: -1->5->3->4->0
##Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if head == None:
            return None
        length = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            length += 1
        return self.sort(head, length)

    def sort(self, head, length):
        if length == 1:
            return head
        head2 = head
        for i in range(int(length / 2)):
            head2 = head2.next
        left = self.sort(head, int(length / 2))
        right = self.sort(head2, length - int(length / 2))
        return self.merge(left, right, int(length / 2), length - int(length / 2))

    def merge(self, left, right, length1, length2):
        dummy = ListNode(0)
        head = dummy
        pointer1 = 0
        pointer2 = 0
        while pointer1 < length1 and pointer2 < length2:
            if left.val < right.val:
                head.next = left
                left = left.next
                pointer1 += 1
                head = head.next
            else:
                head.next = right
                right = right.next
                pointer2 += 1
                head = head.next
        while pointer1 < length1:
            pointer1 += 1
            head.next = left
            left = left.next
            head = head.next
        while pointer2 < length2:
            pointer2 += 1
            head.next = right
            right = right.next
            head = head.next
        head.next = None
        return dummy.next
