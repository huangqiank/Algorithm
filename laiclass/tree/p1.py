## pre order :  left mid right
## in order :  mid left right
## post order :  left right mid


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order(self, node):
        res = []
        if node is None:
            return None
        self.pre_order_help(res, node)
        return res

    def pre_order_help(self, res, node):
        if node is None:
            return res
        self.pre_order_help(res, node.left)
        res.append(node.value)
        self.pre_order_help(res, node.right)

    def in_order_help(self, res, node):
        if node is None:
            return res
        res.append(node.value)
        self.pre_order_help(res, node.left)
        self.pre_order_help(res, node.right)

    def post_order_help(self, res, node):
        if node is None:
            return res
        self.pre_order_help(res, node.left)
        self.pre_order_help(res, node.right)
        res.append(node.value)

    def length(self, node):
        if node is None:
            return 0
        a = self.length(node.left)
        b = self.length(node.right)
        return 1 + max(a, b)

    def symmetric(self, node):
        if node is None:
            return True
        return self.symmetric_help(node.left, node.right)

    def symmetric_help(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node1 is None:
            return False
        if node1.value != node2.value:
            return False
        return self.symmetric_help(node1.left, node2.right) and self.symmetric_help(node1.right, node2.left)

    def bbt(self, node):
        if node is None:
            return 0
        left = self.bbt(node.left)
        right = self.bbt(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    def bst(self, node):
        min_value = -float('inf')
        max_value = float('inf')
        self.bst_help(node, min_value, max_value)

    def bst_help(self, node, min_value, max_value):
        if node.value < min_value:
            return False
        if node.value > max_value:
            return False
        if node.value > min_value and node.value < max_value:
            return self.bst_help(node.left, min_value, node.value) and self.bst_help(node.right, node.value, max_value)


def print_k1_k2(node, k1, k2):
    if not node:
        return
    if node.val > k1 and node.val < k2:
        print(node.val)
        print_k1_k2(node.left, k1, k2)
        print_k1_k2(node.right, k1, k2)
    if node.val < k1:
        print_k1_k2(node.right, k1, k2)
    if node.val > k2:
        print_k1_k2(node.left, k1, k2)


def print_same_level(node):
    res = []
    next_level = [node]
    while next_level:
        n = len(next_level)
        cur_level = []
        while n > 0:
            n -= 1
            node = next_level.pop(0)
            cur_level.append(node)
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        res.extend(cur_level)
    return res


class TreeNode():
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def pre_order(self, node):
        res = []
        self.pre_order_help(res, node)
        return res

    def pre_order_help(self, res, node):
        if node is None:
            return res
        self.pre_order_help(res, node.left)
        res.append(node)
        self.pre_order_help(res, node.right)

    def length(self, node):
        if node is None:
            return 0
        left = self.length(node.left)
        right = self.length(node.right)
        return 1 + max(left, right)

    def symetric(self, node):
        if node is None:
            return True
        return self.symetric_help(node.left, node.right)

    def symetric_help(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return True
        if left.value != right.value:
            return False
        return self.symetric_help(left.left, right.right) and self.symetric_help(left.right, right.left)

    ##bbt: 左右长度不差1
    ## bst 左小右大
    def balanced(self, node):
        if node is None:
            return True
        left = self.balanced(node.left)
        right = self.balanced(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    def bst(self, node):
        if node is None:
            return True
        min_value = -float('inf')
        max_value = float('inf')
        return self.bst_help(node, min_value, max_value)

    def bst_help(self, node, min_value, max_value):
        if node is None:
            return True
        if node.value > max_value or node.value < min_value:
            return False
        return self.bst_help(node.left, min_value, node.value) and self.bst_help(node.right, node.value, max_value)
