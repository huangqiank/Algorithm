'''
Created on Oct 6, 2017

@author: qiankunhuang
'''

class TreeNode:
    def __init__(self,x):
        self.left= None
        self.right=None
        self.val=x
        
def k_large(root,k):
    res=[0]
    count = 0
    k_large_help(root,k,res,count)
    return res.pop()

def k_large_help(root,k,res,count):
    if not root:
        return
    if k == count:
        return res
    k_large_help(root.left,k,res,count)
    count += 1
    res.append(root.val)
    res.pop(0)
    print count,res
    k_large_help(root.right,k,res,count)
    
    
    
root1=TreeNode(10)
root1.left = TreeNode(7)
root1.right = TreeNode(17)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(8)
root1.right.left = TreeNode(11)
root1.right.right = TreeNode(19)


def kthSmallest( root, k):
        s, cur, rank = [], root, 0
        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right
        return float("-inf")

#        10                       3
#      7   17                  1       5
#    3 8   1119             0     2   4  6
#3 7 8 10 11 17 19

print k_large( root1, 1)