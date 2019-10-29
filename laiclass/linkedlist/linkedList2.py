class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class Stack:
    def __init__(self):
        self.size = 0
        self.tail = None

    def push(self, x):
        node = Node(x)
        if self.tail is None:
            self.tail = node
        else:
            node.next = self.tail
            self.tail = node
        self.size += 1

    def pop(self):
        if self.tail is None:
            return
        node = self.tail
        self.tail = self.tail.next
        self.size -= 1
        return node.value


class Queue:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def enqueue(self, x):
        node = Node(x)
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.value


def find_middle(llist):
    cur_head = llist.head
    fast_head = llist.head
    while fast_head != None:
        if fast_head.next is None:
            return cur_head.value
        fast_head = fast_head.next.next
        cur_head = cur_head.next
    return cur_head.value


def merge(head1, head2):
    newHead = Node(0)
    curHead = newHead
    while head1 != None and head2 != None:
        if head1.value >= head2.value:
            curHead.next = head2
            curHead = head2
            head2 = head2.next
        else:
            curHead.next = head1
            curHead = head1
            head1 = head1.next
    if head1 != None:
        curHead.next = head1
    if head2 != None:
        curHead.next = head2
    return newHead.next


def prit(node):
    while node != None:
        print(node.value)
        node = node.next


def parathesis(p):
    a = Stack()
    for i in p:
        if i in ["(", "[", "{"]:
            a.push(i)
        if i == ")":
            if a.size <= 0 or a.pop() != "(":
                return False
        if i == "]":
            if a.size <= 0 or a.pop() != "[":
                return False
        if i == "}":
            if a.size <= 0 or a.pop() != "{":
                return False
    if a.size != 0:
        return False
    return True




class Solution(object):
    def partition(self, head, x):
        small_head = Node(None)
        large_head = Node(None)
        small_dummy = small_head
        large_dummy = large_head
        dummy = head
        while dummy != None:
            if dummy.value > x:
                large_head.next = Node(dummy.value)
                large_head = large_head.next
                dummy = dummy.next
            else:
                small_head.next = Node(dummy.value)
                small_head = small_head.next
                dummy = dummy.next
        small_head.next = large_dummy.next
        return small_dummy.next

class Solution(object):
    def insert(self,head,value):
        node =Node(value)
        dummy = head
        cur_head = head
        if dummy is None:
            node.next = dummy
            return node
        while dummy != None and dummy.next != None:
            if dummy.value <= value and dummy.next.value >= value:
                node.next =  dummy.next
                dummy.next = node
                return cur_head
            elif dummy.value > value:
                node.next = dummy
                return node
            elif dummy.next.value < value:
                dummy = dummy.next
        return cur_head




def palindrom(node):
    head1 = node
    head2 = node
    s= Stack()
    while head1 != None:
        s.push(head1.value)
        head1 = head1.next
    while head2 != None:
        if head2.value != s.pop():
            return False
        else:
            head2 = head2.next
    return True


node1 = Node(0)
node2 = Node(2)
node3 = Node(1)
node4 = Node(0)
global_node = node1
node1.next = node2
node2.next = node3
node3.next = node4
q1 = Queue()
q1.tail = node4
q1.head = node1
def palindrom2(node):
    global global_node
    if node.next is None:
        return node.value == global_node.value
    if palindrom2(node.next):
        global_node = global_node.next
        return node.value == global_node.value
    return False
print(palindrom2(node1))






