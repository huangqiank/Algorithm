'''
Created on Sep 16, 2017

@author: qiankunhuang
'''


class Treenode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x

    def preorder(self):
        res = []
        self.help(res)
        return res

    def help(self, res):
        if self is None:
            return
        res.append(self.value)
        self.help(self.left)
        self.help(self.right)


def sum_root(node, k, cur_sum=0):
    if node is None:
        return False
    cur_sum += node.value
    if cur_sum == k:
        return True
    return sum_root(node.left, k, cur_sum) or sum_root(node.t, k, cur_sum)


node1 = Treenode(3)
node2 = Treenode(2)
node3 = Treenode(4)
node4 = Treenode(-1)
node5 = Treenode(3)
node6 = Treenode(0)
node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node5
##         3
##       2   4
##    -1
##   3
print(sum_root(node1, 7, 0))


def total_sum(node):
    if node is None:
        return False
    cur = 0
    total_sum_help(node, cur)
    return cur


def total_sum_help(node, cur):
    if node is None:
        return 0
    cur += node.sum
    total_sum_help(node.left, cur)
    total_sum_help(node.right, cur)


def sum_to_k(node, k):
    cur = 0
    sum_to_k_help(node, k, cur)


def sum_to_k_help(node, k, cur):
    if node is None:
        return False
    cur += node.value
    if cur == k:
        return True
    return sum_to_k_help(node.left, k, cur) or sum_to_k_help(node.right, k, cur)


def sum_root(node, k, cur_sum=0):
    if node is None:
        return False
    cur_sum += node.value
    if cur_sum == k:
        return True
    return sum_root(node.left, k, cur_sum) or sum_root(node.t, k, cur_sum)