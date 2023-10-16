##86. 分隔链表
##给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
##你应当 保留 两个分区中每个节点的初始相对位置。
##示例 1：
##输入：head = [1,4,3,2,5,2], x = 3
##输出：[1,2,2,4,3,5]
##示例 2：
##输入：head = [2,1], x = 2
##输出：[1,2]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        small = ListNode()
        large = ListNode()
        tmp = head
        small_head = small
        large_head = large
        while tmp:
            if tmp.val < x:
                small.next = tmp
                small = small.next
            else:
                large.next = tmp
                large = large.next
            tmp = tmp.next
        large.next = None
        small_head.next = large_head.next
        return small_head.next


##122
##435
head = [1, 4, 3, 2, 5, 2]
node_list = []
for val in head:
    node_list.append(ListNode(val))
for i in range(len(node_list) - 1):
    node_list[i].next = node_list[i + 1]
s = Solution()
tmp = s.partition(node_list[0], 3)
while tmp:
    print(tmp.val)
    tmp = tmp.next
