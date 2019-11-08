##Algorithm of Insertion Sort:
##Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
##At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
##It repeats until no input elements remain.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        if head is None:
            return
        old_head = head
        old_point = head.next  ## 每次向后一个
        while old_point:
            old_head = head
            while old_head :
                if old_point.val < old_head.next.val:




            old_point = old_point.next





