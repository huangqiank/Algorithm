'''
Created on Oct 1, 2017

@author: qiankunhuang
'''
def remove(A):
    lst=[]
    for fast in A:
        if fast not in ["u","n"]:
            lst.append(fast)
    return "".join(lst)

A="aunsdad"
print(remove(A))
