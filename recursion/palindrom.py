'''
Created on Sep 24, 2017

@author: qiankunhuang
'''
class listnode:
    def __init__(self,value):        
        self.next = None
        self.val = value
nodep0 = listnode(0)
nodep1 = listnode(1)
nodep2 = listnode(2)
nodep3 = listnode(3)
nodep4 = listnode(0)
start = nodep0
nodep0.next = nodep1
nodep1.next = nodep2
nodep2.next = nodep3
nodep3.next = nodep4     

def palindrom(node):
    global start
    if node.next is None:
        if start.val != node.val:
            return False
        return True
    if  palindrom(node.next) is True:
        start = start.next
        if start.val ==node.val:
            return True
        return False
    else:
        return False

print (palindrom(nodep0) )