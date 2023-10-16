##143. 重排链表
##给定一个单链表 L 的头节点 head ，单链表 L 表示为：
##L0 → L1 → … → Ln - 1 → Ln
##请将其重新排列后变为：
##l0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
##不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
##示例 1：
##输入：head = [1,2,3,4]
##输出：[1,4,2,3]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        n = len(node_list)
        begin = 0
        end = n - 1
        pre, next = None, None
        while begin < end:
            node_list[begin].next = node_list[end]
            begin += 1
            if begin == end:
                break
            node_list[end].next = node_list[begin]
            end -= 1
        node_list[begin].next = None
        return node_list[0]


##[1, 2, 3, 4, 5]
## [12543]
##[15243]

##[123456]
## 3,2   3,5   4,None
##mid = 4
##
class Solution2:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        dummy = ListNode()
        dummy.next = head
        mid = self.find_mid(head)
        right = mid.next
        mid.next = None
        right_node = self.reverse(right)

        left_node = head
        self.merge(left_node, right_node)
        return dummy.next

    def merge(self, l1, l2):
        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l1 = tmp1
            l2.next = l1
            l2 = tmp2

    def find_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, node):
        if node is None or node.next is None:
            return node
        end = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return end


s = Solution2()
head = [1, 2, 3, 4,5]
node_list = []
for val in head:
    node_list.append(ListNode(val))
for i in range(len(node_list) - 1):
    node_list[i].next = node_list[i + 1]
tmp = s.reorderList(node_list[0])
while tmp:
    print(tmp.val)
    tmp = tmp.next
