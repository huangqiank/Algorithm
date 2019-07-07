'''
Created on Sep 26, 2017

@author: qiankunhuang
'''
def all_combination(coins,k):
    solution = []
    index = 0
    combination(coins , index , k , solution)

def combination(coins , index, k , solution):
    if index == len(coins):
        if k == 0:
            print solution
        return 
    for j in xrange(0,k/coins[index]+1,1):
        solution.append(j)
        combination(coins , index+1,k-solution[-1]*coins[index],solution)
        solution.pop()
       
coins = [1,2,3,4]
k = 5
all_combination(coins,k)
        
        
        
    