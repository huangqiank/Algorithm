##Algorithm of Insertion Sort:
##Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
##At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
##It repeats until no input elements remain.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insertionSort(head):
    root = ListNode(0)
    root.next = head
    while head.next:
        if head.val <= head.next.val:
            head = head.next
        else:
            q = root
            tmp = head.next
            head.next = head.next.next
            while q.next and q.next.val <= head.next.val:
                q =q.next
            tmp.next = q.next
            q.next = tmp
    return root.next
