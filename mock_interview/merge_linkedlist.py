'''
Created on Oct 21, 2017

@author: qiankunhuang
'''

def merge_linked(head1,head2):
    cur = Node()
    dummy=cur
    while head1 != None and head2 !=None:
        if head1.val<head2.val:
            cur.next =head1
            cur=cur.next
        else:
            cur.next =head2
            cur=cur.next
    return dummy.next

