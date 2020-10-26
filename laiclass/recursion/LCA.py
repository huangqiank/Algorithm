'''
Created on Sep 18, 2017

@author: qiankunhuang
'''


class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


def find_path(start, k, path):
    if start is None:
        return False
    path.append(start)
    if start == k:
        return True
    if find_path(start.left, k, path) or find_path(start.right, k, path):
        return True
    path.pop()
    return False


def find_LCA(start, n1, n2):
    path1 = []
    path2 = []
    if not find_path(start, n1, path1) or not find_path(start, n2, path2):
        return False
    prit(path1)
    prit(path2)
    for i in range(len(path1) - 1, -1, -1):
        if path1[i] in path2:
            return path1[i].val


def prit(path):
    for i in path:
        print(i.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
##    1
##  2   3
##4   5

find_LCA(root, root.left.left, root.left.right)


# print (find_LCA(root,root.left,root))


def find_LCA2(node, k1, k2):
    if node is None:
        return None
    if node.val == k1 or node.val == k2:
        return node
    left = find_LCA2(node.left, k1, k2)
    right = find_LCA2(node.right, k1, k2)
    if left and right:
        return node
    return left if left else right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print(find_LCA2(root,2,4).val)
