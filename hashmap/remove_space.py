'''
Created on Oct 1, 2017

@author: qiankunhuang
'''
def remove_space(A):
    if not A or len(A) == 0:
        return A
    lst = []
    for j in xrange(len(A)):
        if A[j] == " " and (j == 0 or A[j - 1] == " "):
            continue
        lst.append(A[j])
    if lst[-1]  == " ":
        lst.pop()
    return "".join(lst)
A="   abc  ed  ef  "
print (remove_space(A))
###" ".join(A) 在str有" " 时，不会再多加" "的
## 直接return  " ".join(lst) ,补课return lst



        