'''
Created on Jan 20, 2018

@author: qiankunhuang
'''
def remove_adjacent2(a):
    if not a or len(a) <2:
        return a
    n = len(a)
    i = 0
    res=[]
    while i<n:
        if len(res)<2 or res[-1] != a[i] or res[-2] != a[i]:
            res.append(a[i])
            i+=1
        else:
            i+=1
    return ''.join(res)

print (remove_adjacent2('aabbcccba'))
            
    
