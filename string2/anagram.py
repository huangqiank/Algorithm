'''
Created on Oct 2, 2017

@author: qiankunhuang
'''
def anagram(a,b):
    if not a and not b and len(a) == 0 and len(b) == 0:
        return
    A={}
    B={}
    for i in a:
        if i not in A:
            A[i] = 1
        else:
            A[i] += 1
    for j in b:
        if j not in B:
            B[j] = 1
        else:
            B[j] += 1
    if A == B:
        return True
    return False
    
print (anagram("abcdef","bcdefa"))
  
        