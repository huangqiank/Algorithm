'''
Created on Jan 17, 2018

@author: qiankunhuang

'''
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def partition(self, head, target):
      """
      head: ListNode
      target: int
      return: ListNode
      """
      small = ListNode(None)
      small_dummy = small
      large=ListNode(None)
      large_dummy=large
      dummy = head
      while dummy !=None:
        if dummy.val <= target:
            small.next = ListNode(dummy.val)
            small =small.next
            dummy=dummy.next
        else:
            large.next = ListNode(dummy.val)
            large =large.next
            dummy = dummy.next
      small.next = large_dummy.next
      return small_dummy.next
node1=ListNode(3)
node2=ListNode(5)
node3=ListNode(1)
node4=ListNode(2)
node5=ListNode(None)
node1.next = node2
node2.next = node3
node3.next= node4
def prit(node):
    while node != None:
        print node.val
        node=node.next
print prit(Solution().partition(node1,1))
        