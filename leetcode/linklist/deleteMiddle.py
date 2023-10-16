##2095. 删除链表的中间节点
##给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。
#长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。
#对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。
#示例 1：
#输入：head = [1,3,4,7,1,2,6]
#输出：[1,3,4,1,2,6]
#解释：
#上图表示给出的链表。节点的下标分别标注在每个节点的下方。
#由于 n = 7 ，值为 7 的节点 3 是中间节点，用红色标注。
#返回结果为移除节点后的新链表。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        pre = self.find_pre_mid(head)
        if pre.val == -1:
            return None
        if pre and pre.next:
            pre.next = pre.next.next
        return head


    def find_pre_mid(self,node):
        slow= ListNode(-1)
        fast =node
        slow.next = node
        while fast and fast.next:
            fast = fast.next.next
            slow= slow.next
        return slow