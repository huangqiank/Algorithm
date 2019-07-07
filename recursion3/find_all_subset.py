'''
Created on Sep 26, 2017

@author: qiankunhuang
'''
def find_subset(input):
    index = 0
    res = []
    find_all_subset(index,input,res)
def find_all_subset(index,input,res):
    if index == len(input):
        print res
        return
    res.append(input[index])
    find_all_subset(index+1,input,res)
    res.pop()
    find_all_subset(index+1,input,res)
   
    
input=["a","b","c"]
find_subset(input)




    