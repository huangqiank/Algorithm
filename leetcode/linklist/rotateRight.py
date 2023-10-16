##61. 旋转链表
##给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
##示例 1：
##输入：head = [1,2,3,4,5], k = 2
##输出：[4,5,1,2,3]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return
        n = 1
        tmp = head
        while tmp.next:
            n += 1
            tmp = tmp.next
        ## 12
        ## n=2 k =1
        dummy = ListNode()
        dummy.next = head
        if k % n == 0:
            return head
        steps = n - k % n
        while steps > 0:
            dummy = dummy.next
            steps -= 1
        begin = dummy.next  ##2
        dummy.next = None
        tmp.next = head
        return begin





##     1 2 3 4
## p   f
## 1 3  2 
