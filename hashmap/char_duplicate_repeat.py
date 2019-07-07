'''==
Created on Sep 30, 2017

@author: qiankunhuang
'''
def char_duplicate_repeat(str):
    if str is None or len(str) ==0:
        return
    fast = 0
    lst =[]
    while fast < len(str):
        if len(lst) > 0 and str[fast]== lst[-1]:
            c= str[fast]
            while fast < len(str) and c == str[fast]:
                fast += 1
            lst.pop()
        else:
            lst.append(str[fast])
            fast += 1
    return " ".join(lst)
        
            
A="cabbcad"
print char_duplicate_repeat(A)
print len(A)
                  
            
            
        
        
        