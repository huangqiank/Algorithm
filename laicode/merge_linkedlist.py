'''
Created on Feb 27, 2018

@author: qiankunhuang
'''
class Node:
    def __init__(self,x):
        self.value = x
        self.next = None
class linkedlist:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None
    def enqueue(self,value):
        node=Node(value)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size +=1
    def dequeue(self):
        if self.size is None:
            return False
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a
    def value(self):
        return self.value
    def print_linkedlist(self):
        temp = self.head
        while temp:
            print temp.value
            temp=temp.next

## function merge:merge two linked_list and find the new head

def merge(l1,l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.value<=l2.value:
        temp = l1
        temp.next = merge(l1.next,l2)
    else:
        temp = l2
        temp.next = merge(l1,l2.next)
    return temp

## function mergesort:merge linkedlist  
def mergesort(head):
    if head is None or head.next is None:
        return head
    l1,l2 = divide(head)
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    head = merge(l1,l2)
    return head
## divide and find the mid
def divide(head):
    slow= head
    fast = head
    if fast:
        fast = fast.next
    while fast:
        fast =fast.next
        if fast:
            fast=fast.next
            slow=slow.next
    mid = slow.next
    slow.next = None
    return head,mid
list1 = linkedlist()
list1.enqueue(2)
list1.enqueue(3)
list1.enqueue(0)
list1.enqueue(4)

list1.head=mergesort(list1.head)
list1.print_linkedlist()
            