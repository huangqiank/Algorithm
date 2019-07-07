'''
Created on Feb 17, 2018

@author: qiankunhuang
'''

def find(list,k):
    left = 0
    right = len(list)-1
    a1 = list[0]
    a2=list[right]
    while left + 1<right:
        mid= (left+right)/2
        if k == list[mid]:
            return mid
        if k>list[mid]:
            if k<=a2:
                left = mid
            else:
                right =mid
        if k<list[mid]:
            if k>=a1:
                left= mid
            else:
                right =mid
    if list[left] == k:
        return left
    if list[right] == k:
        return right
    return -1

import heapq
def merge(heads):
    k = len(heads)
    if k == 0:
        return 
    new = []
    dummy= None
    cur= None
    dummy.next = cur
    for head in heads:
        heapq.heappush(new,(head.val,head))
    while new:
        node = heapq.heappop(new)
        if node[1]!= None:
            cur.next = node[1]
            cur=  cur.next
        if node[1].next != None:
            heapq.heappush(new,(node[1].next.val,node[1].next))
    return dummy.next                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            
def print_most_right(node):
    res= []
    queue=[node]
    if node is None:
        return 
    while queue:
        n = len(queue)
        this_level = []
        while n>0:
            n-=1
            node = queue.pop(0)
            this_level.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        res.append(this_level[-1])
    return res
def addbinary(a,b):
    s = 0
    for i in xrange(len(a)):
        if a[i]==1:
            s+=2^i
    for j in xrange(len(b)):
        if b[i] == 1:
            s+=2^j
    return
class Treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def pre_order(self):
        res=[]
        self.helper(self,res)
        return res
    def helper(self,res):
        if not self:
            return 
        res.append(self.value)
        self.helper(self.left,res)
        self.helper(self.right,res)

def getsum(root):
    if not root:
        return 0
    res=[0]
    sumhelp(root,res,0)
    return res[0]
def sumhelp(root,res,cur):
    if not root:
        return
    cur=cur*10+root.val
    if not root.left and not root.right:
        res[0]+=cur
    sumhelp(root.left,res,cur)
    sumhelp(root.right,res,cur)
    