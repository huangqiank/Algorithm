'''
Created on Sep 30, 2017

@author: qiankunhuang
'''
def char_duplication(str):
    if not str or len(str) < 2:
        return str
    fast = 0
    lst = []
    while fast < len(str):
        if len(lst) == 0 or lst[-1] != str[fast]:
            lst.append(str[fast])
        fast += 1
    return " ".join(lst)
A="aabbccddaa"
print char_duplication(A)


            
    
        