import operator


class node:
    def __init__(self, x):
        self.value = x
        self.next = None


## 后进先出
class queue():
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def enqueue(self, x):
        new_node = node(x)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1

    def size(self):
        return self.size


def merge(head1, head2):
    new_head = node(0)
    cur = new_head
    tmp1 = head1
    tmp2 = head2
    while tmp1 and tmp2:
        if tmp1.value < tmp2.value:
            cur.next = tmp1
            cur = tmp1
            tmp1 = tmp1.next
        else:
            cur.next = tmp2
            cur = tmp2
            tmp2 = tmp2.next
    if tmp1:
        cur.next = tmp1.next
    if tmp2:
        cur.next = tmp2.next
    return new_head.next


def insert_sorted_linkedlist(head, value):
    insert_node = node(value)
    tmp_head = head
    if tmp_head is None:
        insert_node.next = tmp_head
        return insert_node
    while tmp_head != None:
        if tmp_head.value < insert_node.value and (tmp_head.next != None or tmp_head.value > insert_node.value):
            insert_node.next = tmp_head.next
            tmp_head.next = insert_node
            return head
        elif tmp_head.value > insert_node.value:
            insert_node.next = tmp_head
            return insert_node
        elif tmp_head.next.value < tmp_head.value:
            tmp_head = tmp_head.next


def partition(head, value):
    small = node(None)
    small_tmp = small
    large = node(None)
    large_tmp = large
    tmp = head
    while tmp:
        if tmp.value < value:
            small_tmp.next = node(value)
            small_tmp = small_tmp.next
            tmp = tmp.next
        else:
            large_tmp.next = node(value)
            large_tmp = large_tmp.next
            tmp = tmp.next
    small_tmp.next = large.next
    return small.next


def insert_sorted_linkedlist(head, value):
    insert_node = node(value)
    if head is None:
        insert_node.next = head
        return insert_node
    tmp = head
    while tmp != None:
        if tmp.value <= value and (tmp.next != None or tmp.next.value > value):
            insert_node.next = tmp.next
            tmp.next = insert_node
            return head
        elif tmp.value > value:
            insert_node.next = tmp
            return insert_node
        elif tmp.next.value <= value:
            tmp = tmp.next


class stack():
    def __init__(self):
        self.head = None
        self.size = 0

    def pop(self):
        if self.head is None:
            return
        tmp = self.head.value
        self.head = self.head.next
        self.size -= 1
        return tmp

    def push(self, x):
        insert_node = node(x)
        self.size += 1
        if self.head is None:
            self.head = insert_node
            return
        insert_node.next = self.head
        self.head = insert_node


inputs = [1, 2, 3, "+", "-"]
global_operator = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}


def rev_poland(inputs):
    s = stack()
    for i in inputs:
        if i not in global_operator:
            s.push(i)
        else:
            right = s.pop()
            left = s.pop()
            s.push(global_operator[i](left, right))
    return s.pop()


print(rev_poland([1, 2, 3, "+", "-"]))


class stack():
    def __init__(self):
        self.head = None
        self.size = 0

    def pop(self):
        if self.head is None:
            return
        tmp = self.head.value
        self.head = self.head.next
        self.size -= 1
        return tmp

    def push(self, x):
        insert_node = node(x)
        self.size += 1
        if self.head is None:
            self.head = insert_node
            return
        insert_node.next = self.head
        self.head = insert_node


##  h<-1<-2<-3<-4<-t
##

def palindrom(node, global_node=node):
    if node.next is None:
        return node.val == global_node.val
    if palindrom(node.next, global_node) is True:
        global_node = global_node.next
        return node.value == global_node.value
    else:
        return False


##1->2->3

## 1<-2<-3
def reverse(node):
    if node is None:
        return node
    new_end = reverse(node.next)
    node.next.next = node
    node.next = None
    return new_end
## 1->2->3
## 2-1 -3
def reverse_pair(node):
    if node is None or node.next is None:
        return node
    next_node = node.next
    new = reverse_pair(node.next.next)
    node.next.next = node
    node.next =new
    return next_node







