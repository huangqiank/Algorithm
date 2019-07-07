'''
Created on Feb 18, 2018

@author: qiankunhuang
'''
def memo(func):
    cache={}
    def newFunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return newFunc
def fib(n):
    if n == 0 or n == 1:
        return  n
    return fib(n-1)+fib(n-2)
def func_count(func):
    count,cache = [0],{}
    def newFunc(*args):
        if args not in cache:
            count[0]+=1
            cache[args] = func(*args)
        return cache[args]
    newFunc.num_of_calls=count
    return newFunc