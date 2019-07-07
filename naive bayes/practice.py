'''
Created on Sep 26, 2017

@author: qiankunhuang
'''
class node:
    def __init__(self,value):        
        self.next = None
        self.value = value
def reverse2(node):
    pre = None
    head = node
    while head != None:
        next_node = head.next
        head.next = pre
        pre = head
        head = next_node
    head = pre
    return  head

