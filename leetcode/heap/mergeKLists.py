##23. Merge k Sorted Lists
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.
#Example 1:
#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        n = len(lists)
        dummy = ListNode()
        tmp = dummy
        for i in range(n):
            heapq.heappush(h,(lists[0].val,lists[0]))
        while  h :
            val,node = heapq.heappop(h)
            dummy.next = ListNode(val)
            dummy = dummy.next
            if node.next :
                heapq.heappush(h,(node.next.val,node.next))
        return tmp.next





class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h= []
        tmp = ListNode()
        dummy = tmp
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(h,[lists[i].val,i])
        while h:
            val,i = heapq.heappop(h)
            dummy.next = ListNode(val)
            dummy = dummy.next
            if lists[i].next :
                heapq.heappush(h,[lists[i].next.val,i])
                lists[i] = lists[i].next
        return tmp.next