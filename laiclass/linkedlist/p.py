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


class stack():
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, x):
        new = node(x)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        self.size += 1

    def pop(self):
        if self.head is None:
            return
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value



