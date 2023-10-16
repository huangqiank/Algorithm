##24. 两两交换链表中的节点
##你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
##示例 1：
##输入：head = [1,2,3,4]
##输出：[2,1,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ##a-b-c-d
        ##b-a - d-c
        ## node.next.next = node
        ## node.next = node.next.next.next
        ##f(node.next.next)
        ##return node.next.next.next
        if not head or head.next is None:
            return head
        end = self.swapPairs(head.next.next)
        next = head.next
        head.next.next = head
        head.next = end
        return next