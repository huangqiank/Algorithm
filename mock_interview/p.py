'''
Created on Feb 22, 2018

@author: qiankunhuang
'''

#1   
def find_max(matrix):
    ## res = [count the number of 1, row ]
    res= [0,0]   
    n = len(matrix)
    if not matrix:
        return
    if n == 0:
        return
    for i in xrange(n):
        if sum(matrix[i])>res[0]:
            res = [sum(matrix[i]),i]
        if sum(matrix[i]) ==res[0]:
            res.append([sum(matrix[i]),i])
    print res

#2
#define stack
class listnode:
    def __init__(self,value):        
        self.next = None
        self.value = value
class stack:
    def __init__(self):
        self.size = 0
        self.tail = None
    def push(self,value):
        node=listnode(value)
        if self.tail == None:
            self.tail = node
        else:
            node.next = self.tail
            self.tail = node
        self.size +=1
    def pop(self):
        if self.size == 0:
            return False
        else:
            a = self.tail.value
            self.tail= self.tail.next
        self.size -= 1
        return a
    def value(self):
        return self.value
        
import operator
Global_Operator = {'(','[','{'}
def parentheses(str):
#Use stack to store '(','[','{' , when we see ')',']','}', pop and compare
#push:
###case 1: before '{' should be '{'
###case 2 : before '[' should be '{'
###case 3 : before '(' should be '{' or '['
    paren_stack = stack()
    for x in str:
        if x in Global_Operator:
            if paren_stack.size == 0:
                paren_stack.push(x)
            else:
                if x == '{' and  paren_stack.tail.value != '{':
                    return False
                if x == '(' and  paren_stack.tail.value not in ['{','[']:
                    return False
                if x == '[' and  paren_stack.tail.value !='{':
                    return False       
            if paren_stack.size==0:
                    return False
            if x == ')' and paren_stack.pop()!='(':
                    return False
            if x == ']' and  paren_stack.pop()!='[':
                    return False
            if x == ')' and  paren_stack.pop()!='(':
                    return False
    return True

#3
set.add([0,0]);
direction = [[-1,0],[1,0],[0,1],[0,-1]]

def dfs(x,y,set):
#direction: [left,right,up,down]=[[-1,0],[1,0],[0,1],[0,-1]]
#Function move is known 
#Use dfs to find all the node and store it in set. The set size is the area.
    for i in xrange(4):
        newX = x+direction[i][0]
        newY = y + direction[i][1]
        if [newX, newY] in set:
            continue
        if not move(i):
            continue 
        set.add([newX, newY])
        dfs(newX, newY, set)
    return set.size();
#4

import heapq
def find_interval(matrix):
# Assumed the input is a matrix
# Use minheap to find the smallest interval:
# The size of the minheap is the same size as the matrix length,
# The element in the minheap is [number,index,array]
# Use max_value,length to store the length of the smallest interval
# Only if the size of the new interval is smaller than the older one, we insert it in the heap.
# Or until one array is empty : index > len(array)  return 

    if not matrix:
        return
    if len(matrix)==0:
        return 
    n = len(matrix)
    res=[]
    for i in range(n):
        heapq.heappush(res,(matrix[i][0],0,matrix[i]))
    max_value = max(res)
    length =  max_value -res[0]
    pair = res[0]
    while pair[1]+1<len(pair[2]):
        pair =res[0]
        max_value=  max(max_value,pair[2][pair[1]+1])
        if max_value-res[0]<length:
            length = max_value-res[0]
            heapq.heappop(res)
            heapq.heappush(res,(pair[2][pair[1]+1],pair[1]+1,pair[2]))
        else:
            return (res[0],max(res))
    return (res[0],max_value )
        
    
                


           