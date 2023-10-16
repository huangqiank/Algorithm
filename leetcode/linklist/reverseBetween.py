##92. 反转链表 II
##给你单链表的头指针 head 和两个整数 left 和 right ，
## 其中 left <= right 。
## 请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
##示例 1：
##输入：head = [1,2,3,4,5], left = 2, right = 4
##输出：[1,4,3,2,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for i in range(left - 1):
            pre = pre.next
        right_node = pre
        for j in range(right - left + 1):
            right_node = right_node.next
        ###  pre  begin          right
        left_node = pre.next
        next = right_node.next
        pre.next = None
        right_node.next = None
        self.reverse(left_node)
        pre.next = right_node
        left_node.next = next
        return dummy.next

    def reverse(self, node):
        if node is None or node.next is None:
            return node
        end = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return end
s = Solution()
head = [1,2,3,4,5]
node_list = []
for val in head:
    node_list.append(ListNode(val))
for i in range(len(node_list) - 1):
    node_list[i].next = node_list[i + 1]
print(s.reverseBetween(node_list[0],0,2).val)
