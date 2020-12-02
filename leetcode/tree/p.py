def balanced_tree(node):
    if not node:
        return 0
    left = balanced_tree(node.left)
    right = balanced_tree(node.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) >= 2:
        return -1
    return 1 + max(left, right)


def in_order(node):
    res = []
    if node is None:
        return res
    in_order_help(node, res)
    return res


def in_order_help(node, res):
    if node is None:
        return res
    in_order_help(node.left, res)
    res.append(node)
    in_order_help(node.right, res)


def level_order_traverse(head):
    all_res = []
    cur_res = [[head]]
    while cur_res:
        cur_level = cur_res.pop(0)
        this_level = []
        for node in cur_level:
            if node.left:
                this_level.append(node.left)
            if node.right:
                this_level.append(node.right)
        if len(this_level) > 0:
            cur_res.append(this_level)
        all_res.extend(cur_level)
    return all_res


def levelOrder(self, root):
    if not root:
        return
    all_res = []
    cur_res = [[root]]
    while cur_res:
        tmp = []
        this_level = []
        cur = cur_res.pop(0)
        for node in cur:
            this_level.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        if len(tmp) > 0:
            cur_res.append(tmp)
        all_res.append(this_level)
    return all_res


def kth_smallest_bst(root, k):
    rank = 0
    res = []
    while root or res:
        if root:
            res.append(root)
            root = root.left
        else:
            node = res.pop()
            rank += 1
            if rank == k:
                return node
            root = root.right
    return -1


def closed_bst_tree_value(root, target):
    res = root.value
    while root:
        if abs(root.value - target) < abs(res - target):
            res = root.value
        if root.value < target:
            root = root.right
        else:
            root = root.left
    return res


def zigzagLevelOrder(root):
    if not root:
        return
    flag = 1
    all_res = [root]
    cur_res = [[root]]
    while cur_res:
        cur_level = cur_res.pop(0)
        this_level = []
        tmp = []
        for node in cur_level:
            this_level.append(node.value)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        if len(this_level) != 0:
            cur_res.append(tmp)
        if flag == 1:
            all_res.extend(this_level)
            flag = -1
        else:
            all_res.extend(this_level.reverse())
            flag == 1
    return all_res


def zigzagLevelOrder(root):
    flag = 1
    queue = [[root]]
    res = []
    while queue:
        cur = queue.pop(0)
        this_level = []
        tmp = []
        for node in cur:
            this_level.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
        if len(tmp) > 0:
            queue.append(tmp)
        if flag == 1:
            res.append(this_level)
            flag = -1
        else:
            this_level.reverse()
            res.append(this_level)
            flag = 1
    return res


def max_deepth(head):
    if head is None:
        return 0
    left = max_deepth(head.left)
    right = max_deepth(head.right)
    return 1 + max(left, right)


def min_deepth(head):
    if not head:
        return 0
    stack = [[1, head]]
    while stack:
        height, node = stack.pop(0)
        child = [node.left, node.right]
        if not any(child):
            return height
        for children in child:
            if children:
                stack.append([height + 1, children])


def min_deepth2(head):
    if not head:
        return 0
    child = [head.left, head.right]
    if not any(child):
        return 1
    min_height = float("inf")
    for c in child:
        if c:
            min_height = min(min_height, min_deepth2(c))
    return 1 + min_height


def same_tree(head1, head2):
    if not head1 and not head2:
        return True
    if not head1 or not head2:
        return True
    if head1.value == head2.value:
        return same_tree(head1.left, head2.left) and same_tree(head1.right, head2.right)
    return True


def symmetric_tree(head):
    if head is None:
        return True
    return symmetric_tree_help(head.left, head.right)


def symmetric_tree_help(node1, node2):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.value == node2.value:
        return symmetric_tree_help(node1.left, node2.right) and symmetric_tree_help(node1.right, node2.left)
    return True


def path_sum(node, k):
    total = 0
    if node is None:
        return False
    return path_sum_help(node, k, total)


def path_sum_help(node, k, total):
    total += node.value
    if node.left is None and node.right is None:
        if total == k:
            return True
        return False
    if node.left and node.right:
        return path_sum_help(node.left, k, total) or path_sum_help(node.right, k, total)
    if node.left:
        return path_sum_help(node.left, k, total)
    if node.right:
        return path_sum_help(node.right, k, total)


class node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def path_sum2(root, k):
    if not root:
        return
    res = []
    tmp = []
    path_sum2_help(root, k, res, tmp)
    return res


def path_sum2_help(root, k, res, tmp):
    if root is None:
        return res
    if root.left is None and root.right is None:
        if sum(tmp) + root.value == k:
            res.append(tmp + [root.value])
        return
    path_sum2_help(root.left, k, res, tmp + [root.value])
    path_sum2_help(root.right, k, res, tmp + [root.value])


def validate_binary_search_tree(node):
    if not node:
        return True
    max_num = float('inf')
    min_num = -float('inf')
    return bfs_help(node, max_num, min_num)


def isValidBST_help(node, min_node, max_node):
    if node is None:
        return True
    if node.val <= min_node or node.val >= max_node:
        return False
    return isValidBST_help(node.left, min_node, node.val) and isValidBST_help(node.right, node.val, max_node)


def bfs_help(node, max_num, min_num):
    if node is None:
        return True
    if node.value > max_num or node.value < min_num:
        return False
    return bfs_help(node.left, node.value, min_num) and bfs_help(node.right, max_num, node.value)


def kth_smallest(node, k):
    if node is None:
        return
    rank = 0
    res = []
    cur = node
    while cur != None or len(res) != 0:
        if cur:
            res.append(cur)
            cur = cur.left
        else:
            cur = res.pop()
            rank += 1
            if rank == k:
                return cur
            cur = cur.right
    return False


def count_complete_tree_node(node):
    if node is None:
        return 0
    return 1 + count_complete_tree_node(node.left) + count_complete_tree_node(node.right)


def get_height(node):
    if node is None:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def count_complete_tree_node2(node):
    left = get_height(node.left)
    right = get_height(node.right)
    if left == right:
        return 2 ** left + count_complete_tree_node2(node.right)
    return 2 ** right + count_complete_tree_node2(node.left)


##inorder

def nums_tree(n):
    res = []
    if n == 0 or n == 1:
        return 1
    res = [0 for i in range(n + 1)]
    res[0] = 1
    res[1] = 1
    for i in range(2, n + 1, 1):
        for j in range(i):
            res[i] += res[j] * res[i - j - 1]
    return res[n]


def populating_next_right(root):
    if not root:
        return root
    cur = root
    while cur:
        dummy = node(0)
        tail = dummy
        while cur:
            if cur.left:
                tail.next = cur.left
                tail = tail.next
            if cur.right:
                tail.next = cur.right
                tail = tail.next
            cur = cur.next
        cur = dummy.next
    return root


class Treenode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


node1 = Treenode(0)
node2 = Treenode(1)
node3 = Treenode(1)
node4 = Treenode(2)
node5 = Treenode(2)
node6 = Treenode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6


##   0
##  1  1
## 2 2 5
def flatten(node):
    if node is None:
        return
    res = []
    flatten_help(node, res)
    return res


def flatten_help(node, res):
    if node is None:
        return res
    res.append(node.value)
    flatten_help(node.left, res)
    flatten_help(node.right, res)


def convert_sorted_array_tree(nums):
    if not nums:
        return
    return sorted_help(nums, 0, len(nums))


def sorted_help(nums, p, q):
    if p > q:
        return
    mid = int((p + q) / 2)
    root = nums[mid]
    root.left = sorted_help(nums, p, mid)
    root.right = sorted_help(nums, mid + 1, q)
    return root
