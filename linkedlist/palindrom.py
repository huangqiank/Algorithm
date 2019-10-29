'''
Created on Sep 10, 2017

@author: qiankunhuang
'''
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


##后进先出
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, x):
        node = Node(x)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.head == None:
            return
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a


##先进后出
class queue:
    def __init__(self):
        self.size = 0
        self.tail = None
        self.head = None

    def dequeue(self):
        if self.head == None:
            return
        else:
            a = self.head.value
            self.head = self.head.next
        self.size -= 1
        return a

    def enqueue(self, x):
        node = Node(x)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


def palindrom(node):
    S = Stack()
    head1 = node
    head2 = node
    while head1 != None:
        S.push(head1.value)
        head1 = head1.next
    while head2 != None:
        if S.pop() != head2.value:
            return False
        head2 = head2.next
    return True


def palindrom2(node):
    global global_node
    if node.next == None:
        return global_node.value == node.value
    if palindrom2(node.next):
        global_node = global_node.next
        return global_node.value == node.value
    else:
        return False


node1 = Node(0)
node2 = Node(2)
node3 = Node(2)
node4 = Node(0)
global_node = node1
node1.next = node2
node2.next = node3
node3.next = node4
q1 = queue()
q1.tail = node4
q1.head = node1

print(palindrom(node1))
print(palindrom2(node1))
