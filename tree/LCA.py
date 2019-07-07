class node:
    def __init__(self,x):
        self.left = None
        self.right = None
        self.val = x


def LCA(start,n1,n2):
    if start is None:
        return None
    if start.val == n1.val or start.val == n2.val:
        return start
    left = LCA(start.left,n1,n2)
    right = LCA(start.right,n1,n2)
    if left and right:
        return start
    if left:
        return left
    if right:
        return right
        
        
     
     