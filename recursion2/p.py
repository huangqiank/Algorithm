'''
Created on Dec 8, 2017

@author: qiankunhuang
'''




def dfs_preorder(node):
    if node is None:
        return
    res=[]
    help2(node,res)
def help2(node,res):
    if node is None:
        return res
    res.append(node.value)
    help2(node.left,res)
    help2(node.right,res)
    

    
def find_parathensis(n):
    left= 0
    right = 0
    res=[]
    help4(left,right,res,n)
def help4(left,right,res,n):
    if left == n and right == n:
        print res
        return
    if left< n:
        res.append("(")
        help4(left+1,right,res,n)
        res.pop()
    if right<left:
        res.append(")")
        help4(left,right+1,res,n)
        res.pop()
find_parathensis(3)
        
    

    
        
    
    
    
        
    
    
    
            
            
        
    

        
        
        
    
        
    
    