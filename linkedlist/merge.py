'''
Created on Sep 9, 2017

@author: qiankunhuang
'''


class Listnode:
    def __init__(self, value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def enqueu(self, value):
        node = Listnode(value)
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return False
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a

    def value(self):
        return self.value


def merge(head1, head2):
    new_head = Listnode(0)
    cur_head = new_head
    while head1 != None and head2 != None:
        if head1.value <= head2.value:
            cur_head.next = head1
            cur_head = head1
            head1 = head1.next
        else:
            cur_head.next = head2
            cur_head = head2
            head2 = head2.next
    if head1 != None:
        cur_head.next = head1
    else:
        cur_head.next = head2
    return new_head.next


def prit(node):
    while node != None:
        print(node.value)
        node = node.next


node1 = Listnode(0)
node2 = Listnode(2)
node3 = Listnode(4)
node1.next = node2
node2.next = node3
q1 = Queue()
q1.tail = node1
q1.head = node3
node4 = Listnode(1)
node5 = Listnode(3)
node6 = Listnode(5)
node4.next = node5
node5.next = node6
q2 = Queue()
q2.tail = node4
q2.head = node6

prit(merge(node1, node4))
