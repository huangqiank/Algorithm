'''
Created on Jan 20, 2018

@author: qiankunhuang
'''
def remove(a):
    n = len(a)
    i = 0
    if not a or len(a)==0:
        return a
    res=[]
    while i< n:
        if len(res)==0 or res[-1] != a[i]:
            res.append(a[i])
            i+=1
        else:
            i+=1
    return ''.join(res)
print remove('aaaabbbc')
            
            