import operator


class node():
    def __init__(self, x):
        self.value = x
        self.next = None


def find_middle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
    if fast == None or fast.next == None:
        return slow


def insert_sorted_linkedlist(head, value):
    insert_node = node(value)
    tmp = head
    if tmp == None:
        insert_node.next = tmp
        return insert_node
    while tmp != None:
        if tmp.value <= value and (tmp.next != None or tmp.next.value > value):
            insert_node.next = tmp.next
            tmp.next = insert_node
            return head
        if tmp.value > value:
            insert_node.next = tmp
            return insert_node
        elif tmp.next.value <= value:
            tmp = tmp.next


##先进先出
class queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enque(self, x):
        new = node(x)
        self.size += 1
        if self.tail is None:
            self.tail = new
            self.head = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if self.head is None:
            return
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


class stack():
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new = node(value)
        self.size += 1
        if self.head is None:
            self.head = new
            return
        new.next = self.head
        self.head = new

    def pop(self):
        if self.head is None:
            return
        value = self.head.value
        self.head = self.head.next
        return value


def palindrom(node):
    tmp1 = node
    tmp2 = node
    s = stack()
    while tmp1 != None:
        s.push(tmp1)
        tmp1 = tmp1.next
    while tmp2 != None:
        if tmp2 != s.pop():
            return False
        tmp2 = tmp2.next


def find_mid(head):
    slow = head
    fast = head
    if fast is None or fast.next is None:
        return slow
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


##    tmp
##
##
def insert_sorted_linkedlist(head, value):
    insert_node = node(value)
    tmp = head
    if tmp is None or tmp.value > value:
        insert_node.next = tmp
        return insert_node
    while tmp:
        if tmp.value <= value and tmp.next is None:
            tmp.next = insert_node
            return tmp
        if tmp.value <= value and tmp.next.value <= value:
            tmp = tmp.next
        if tmp.value <= value and tmp.next.value > value:
            next_node = tmp.next
            tmp.next = insert_node
            insert_node.next = next_node
            return head


def palindrom(head):
    s = stack()
    tmp = head
    while tmp:
        s.push(tmp)
        tmp = tmp.next
    while head:
        if head != s.pop():
            return False
        head = head.next
    return True


def partition(head, x):
    small = node(0)
    small_tmp = small
    large = node(0)
    large_tmp = large
    head_tmp = head
    while head_tmp != None:
        if head_tmp.value < x:
            small_tmp.next = node(head_tmp.value)
            head_tmp = head_tmp.next
            small_tmp = small_tmp.next
        else:
            large_tmp.next = node(head_tmp.value)
            head_tmp = head_tmp.next
            large_tmp = large_tmp.next
    small.next.next = large
    return small_tmp.next


operator_dict = {"+": operator.sub, '*': operator.matmul, '-': operator.sub(), '/': operator.floordiv}


def polan(alist):
    s = stack()
    for item in alist:
        if item in operator_dict:
            s.push(item)
        else:
            right = s.pop()
            left = s.pop()
            s.push(operator_dict[item](right, left))
    return s.pop()


def parathesis(alist):
    s = stack()
    for item in alist:
        if item in ["(", "[", "{"]:
            s.push(item)
            continue
        if item == "]" and (len(s) == 0 or s.pop() != "["):
            return False
        if item == ")" and (len(s) == 0 or s.pop() != "("):
            return False
        if item == "}" and (len(s) == 0 or s.pop() != "{"):
            return False
    if len(s) != 0:
        return False
    return True


def reverse(node):
    if node is None or node.next is None:
        return node
    new_end = reverse(node.next)
    node.next.next = node
    node.next = None
    return new_end


def reverse_pair(node):
    if node is None or node.next is None:
        return node
    next_node = node.next
    next_end = reverse_pair(node.next.next)
    node.nex.next = node
    node.next = next_end
    return next_node

