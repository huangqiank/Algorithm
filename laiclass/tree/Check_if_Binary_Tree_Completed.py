'''
Created on Jan 18, 2018

@author: qiankunhuang
'''
class Solution(object):
    def isCompleted(self, root):
        if root is None:
          return True
        res=[]
        self.help(res,root)
        if '#' in res:
          for i in range(res.index('#'),len(res),1):
              if res[i]!='#':
                return False
        return True
    def help(self,res,root):
      if root is None:
        return 
      res.append(root.val)
      self.help(res,root.left)
      self.help(res,root.right)