'''
Created on Sep 9, 2017

@author: qiankunhuang
'''
class treenode:
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
    
            
            