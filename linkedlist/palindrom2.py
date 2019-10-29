'''
Created on Sep 10, 2017

@author: qiankunhuang
'''
class listnode:
    def __init__(self,value):        
        self.next = None
        self.val = value
nodep0 = listnode(0)
nodep1 = listnode(1)
nodep2 = listnode(2)
nodep3 = listnode(1)
nodep4 = listnode(0)
global_node = nodep0
nodep0.next = nodep1
nodep1.next = nodep2
nodep2.next = nodep3
nodep3.next = nodep4
def is_pal(node):
    global global_node
    if node.next is None:
        return global_node.val == node.val
    if is_pal(node.next) is True:
        global_node = global_node.next
        return global_node.val == node.val  
    else:
        return False
     
print (is_pal(nodep0))



def is_pal2(node,global_node=nodep0):
    if node.next is None:
        return global_node.val == node.val
    if is_pal2(node.next,global_node) is True:
        global_node = global_node.next
        return global_node.val == node.val
    else:
        return False 
print (is_pal2(nodep0 , global_node=nodep0))

