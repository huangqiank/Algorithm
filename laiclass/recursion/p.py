def fib(n):
    nums = [0, 1]
    if n < 2:
        return nums[n]
    for i in range(2, n):
        nums[i] = nums[i - 1] + nums[i - 2]
    return nums[i]


def reversed(node):
    if node is None or node.next is None:
        return node
    end = reversed(node.next)
    node.next.next = node
    node.next = None
    return end


def reversed_pair(node):
    if node is None or node.next is None:
        return node
    next_next = node.next
    next_node = reversed_pair(node.next.next)
    node.next.next = node
    node.next = next_node
    return next_next


def print_same_level(node):
    res = []
    this_level = [node]
    while this_level:
        n = len(this_level)
        queue = []
        while n > 0:
            node = this_level.pop()
            n -= 1
            if node.left:
                this_level.append(node.left)
            if node.right:
                this_level.append(node.right)
            queue.append(node)
        res.extend(queue)
    return res


def symmetric(node):
    if node is None:
        return True
    return symmetric_help(node.left, node.right)


def symmetric_help(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.value != node2.value:
        return False
    return symmetric_help(node1.left, node2.right) and symmetric_help(node1.right, node2.left)

