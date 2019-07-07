'''
Created on Jan 25, 2018

@author: qiankunhuang
'''
def remove(s):
    res=[]
    i = 0
    while i <len(s):
        if len(res) != 0 or (res[-1] ==' '  and s[i] == ' '):
            i+=1
        else:
            res.append(s[i])
            i+=1
    if res[-1] == " ":
        res.remove(-1)
    return ' '.join(res)
def remove2(s):
    lst =list(s)
    i=0
    j=0
    while j<len(lst):
        if lst[j] != ' ' or (j!=0 or lst[j-1] !=' '):
            lst[i] = lst[j]
            i+=1
        j+=1
    if lst[i] ==' ':
        i-=1
    return lst[:-1]
a='abs'
print list(a)
            
            
        