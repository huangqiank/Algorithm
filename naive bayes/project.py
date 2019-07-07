'''
Created on Sep 24, 2017

@author: qiankunhuang
'''
class treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def find_root(input,index,solution):
    if index == len(input):
        print solution
        return
    solution.append([input[index]])
    solution.append()
    index += 1
    find_root(input,index,solution)
     
        
        
    