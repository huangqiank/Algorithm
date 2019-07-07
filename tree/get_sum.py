'''
Created on Feb 18, 2018

@author: qiankunhuang
'''
def getsum(root):
    if not root:
        return 0
    res=[0]
    sumhelp(root,res,0)
    return res[0]
def sumhelp(root,res,cur):
    if not root:
        return
    cur = cur*10+root.val
    if not root.left and not root.right:
        res[0]+=cur
    sumhelp(root.left,res,cur)
    sumhelp(root.right,res,cur)
    