def fibonacci(i):
    nums = [0, 1]
    if i < 3:
        return nums[i]
    for j in range(2, i + 1):
        nums.append(nums[j - 1] + nums[j - 2])
    return nums[i]


def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i - 2) + fibonacci(i - 1)


class Node():
    def __init__(self, x):
        self.value = x
        self.next = None


## ??? 错在哪？

def reversed_linklist(node):
    if node is None or node.next is None:
        return node
    end = reversed_linklist(node.next)
    node.next.next = None
    end.next = node
    return end


def reversed_linklist(node):
    if node is None or node.next is None:
        return node
    end = reversed_linklist(node.next)
    node.next.next = node
    node.next = None
    return end


# 12 34

# 21 43
def reversePair(node):
    if node is None or node.next is None:
        return node
    next_next = node.next
    new = reversePair(node.next.next)
    node.next = new
    next_next.next = node
    return next_next


def reverse_pair_by_pair(node):
    if node is None or node.next is None:
        return node
    new = reverse_pair_by_pair(node.next.next)
    next_next = node.next
    node.next = new
    next_next.next = node
    return next_next


def reverse_pair(node):
    if node is None or node.next is None:
        return node
    next_next = node.next
    new = reverse_pair(node.next.next)
    node.next = new  ## a--->d
    next_next.next = node  ## b--->a
    return next_next
