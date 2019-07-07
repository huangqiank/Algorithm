'''
Created on Oct 16, 2017

@author: qiankunhuang
'''
import random
def one_ou_of_all(a):   
    s=[]
    solution = s[0]
    i = 1
    while True:
        i+=1
        r=random.randint(0,i-1,1)
        if r == 0:
            solution= s[i-1]
            return solution    #(if some one ask)
def k_out_of_al(a):
    s=[]
    solution =s[0:100]
    i = 0
    while True:
        i+=1
        r=random.randint(0,i-1,1)
        if r <100:
            solution[r]= s[i-1]
            return solution 