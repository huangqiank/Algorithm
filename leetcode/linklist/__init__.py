##206. 反转链表
#给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#示例 1：
#输入：head = [1,2,3,4,5]
#输出：[5,4,3,2,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    ## a -->b
    ## b - > a - > None
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        end=self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return end
