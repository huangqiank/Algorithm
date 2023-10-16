##25. K 个一组翻转链表
##给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
##k 是一个正整数，它的值小于或等于链表的长度。
##如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 进阶：
##你可以设计一个只使用常数额外空间的算法来解决此问题吗？
##你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
##示例 1：
##输入：head = [1,2,3,4,5], k = 2
##输出：[2,1,4,3,5]
##示例 2：
##输入：head = [1,2,3,4,5], k = 3
##输出：[3,2,1,4,5]
##示例 3：
##输入：head = [1,2,3,4,5], k = 1
##输出：[1,2,3,4,5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## abcd
## dcba

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ## 0  1  2  3  4
        l = ListNode()
        l.next = head
        pre = l
        ## 0  1  2      3 4 5 6 7 8
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return l.next
            next = tail.next
            tail.next = None
            l1, l2 = self.reverse(head, )
            pre.next = l1
            l2.next = next
            pre =
            head =

        return l.next

    def reverse(self, begin):
        cur = begin
        pre = None
        while begin != None:
            next = begin.next
            begin.next = pre
            pre = begin
            begin = next
        return tail, cur


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while head:
            tail = tmp
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            head, tail = self.reverse(head,tail)
            tmp.next = head
            tmp = tail
            head = tail.next
        return dummy.next



    def reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return tail, head


a={1:[2,3]}
a[1].