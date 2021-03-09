class Treenode():
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

    def pre_order(self, node):
        res = []
        if node is None:
            return
        self.help(res, node)
        return res

    def help(self, res, node):
        if not node:
            return
        res.append(node.value)
        self.help(res, node.left)
        self.help(res, node.right)


def bbt(node):
    if node is None:
        return 0
    left = bbt(node.left)
    right = bbt(node.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)


def bst(node):
    max_value = float("inf")
    min_value = -float("inf")
    if node is None:
        return True
    return bst_help(node, min_value, max_value)


def bst_help(node, min_value, max_value):
    if node is None:
        return True
    if node.val < min_value or node.val > max_value:
        return False
    if node.val > min_value and node.val < max_value:
        return bst_help(node.left, min_value, node.value) and bst_help(node.right, node.value, max_value)


def print_same_level(node):
    res = []
    next_level = [node]
    while next_level:
        n = len(next_level)
        this_level = []
        while n > 0:
            n -= 1
            node = next_level.pop(0)
            if node.left != None:
                next_level.append(node.left)
            if node.right != None:
                next_level.append(node.right)
            this_level.append(node)
        res.extend(this_level)
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
    return symmetric_help(node1.left, node2.left) and symmetric_help(node1.right, node2.right)


def reverse(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    reverse(node.left)
    reverse(node.right)


def lca(node, n1, n2):
    if node is None:
        return None
    if node == n1 or node == n2:
        return node
    left = lca(node.left, n1, n2)
    right = lca(node.right, n1, n2)
    if left and right:
        return node
    if left:
        return left
    if right:
        return right


def kth_smallest(node, k):
    res, cur, rank = [], node, 0
    while res or cur:
        if cur.left:
            res.append(cur)
            cur = cur.left
        else:
            cur = res.pop()
            rank += 1
            if rank == k:
                return cur.value
            cur = cur.right
    return -1



