##148. 排序链表
##给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
##示例 1：
##输入：head = [4,2,1,3]
##输出：[1,2,3,4]
##示例 2：


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if not head:
            return head
        tail = None
        return self.sort(head, tail)

    def sort(self, head, tail):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head

        slow, fast = head, head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.sort(head, mid), self.sort(mid, tail))

    def merge(self, l1, l2):
        tmp = ListNode()
        pre = tmp
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return pre.next
