'''
Created on Sep 18, 2017

@author: qiankunhuang
'''


def fib(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


def fib2(i, s=[0, 1]):
    if i == 0:
        return 0
    if i == 1:
        return 1
    for j in range(2, i + 1):
        s.append(s[j - 1] + s[j - 2])
    return s[i]


print(fib(20))
print(fib2(100))
