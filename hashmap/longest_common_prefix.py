'''
Created on Oct 8, 2017

@author: qiankunhuang
'''

def longest_common_prefix(str):
    if not str:
        return ""
    shortest = min(str,key=len)
    for i, ch in enumerate(shortest):
        for other in str:
            if other[i] != ch:
                return shortest[:i]
    return shortest
            
            
A=["abcd","abcd","ab"]
print longest_common_prefix(A)