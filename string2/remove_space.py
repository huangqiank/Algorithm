'''
Created on Jan 20, 2018

@author: qiankunhuang
'''
def remove_space(a):
    if not a or len(a) == 0:
        return a
    i=0
    n=len(a)
    res=[]
    while i<n:
        if len(res) ==0 or res[-1] != ' ' or a[i] !=' ':
            res.append(a[i])
            i+=1
        else:
            i+=1
    if res[-1] == ' ':
        res.pop()
    if len(res)>0:
        if res[0] == ' ':
            res.pop(0)
    return ''.join(res)
print (remove_space(' a b c d'))
            