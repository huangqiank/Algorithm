##2. 两数相加
#给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#请你将两个数相加，并以相同形式返回一个表示和的链表。
#你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#示例 1：
#输入：l1 = [2,4,3], l2 = [5,6,4]
#输出：[7,0,8]
#解释：342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp=ListNode(0)
        tail=tmp
        c = 0
        while l1 != None or l2 != None:
            v1,v2=0,0
            if l1 != None:
                v1 = l1.val
                l1 = l1.next
            if l2 != None:
                v2=l2.val
                l2=l2.next
            total = v1+v2+c
            tail.next= ListNode(total%10)
            tail=tail.next
            c= int(total/10)
        if c != 0 :
            tail.next= ListNode(c)
        return tmp.next