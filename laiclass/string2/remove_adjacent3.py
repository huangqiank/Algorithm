'''
Created on Jan 20, 2018

@author: qiankunhuang
'''
def remove(a):
    n=len(a)
    i=0
    res=[]
    while i<n:
        if len(res) != 0 and res[-1] == a[i]:
            k =res[-1] 
            while i<n and a[i]==k:
                i+=1
            res.pop()
        else:
            res.append(a[i])
            i+=1
    return ''.join(res)
print (remove('aabbccba'))

    