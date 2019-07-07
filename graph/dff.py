'''
Created on Sep 23, 2017

@author: qiankunhuang
'''
dif = -1
res = []
def find_max_difference(node):
    global dif
    global res
    if node is None:
        return 0
    left  = height(node.left)
    right  = height(node.right)
    if abs(left - right) > dif:
        res.append(node)
        dif = abs(left - right)
    return 1 + max(left,right