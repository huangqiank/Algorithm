'''
Created on Oct 21, 2017

@author: qiankunhuang
'''
def determine_substr(a,b):
    k1 = len(a)-1
    k2= len(b)-1
    if k1<k2:
        return -1
    i = 0
    while i < k2-k1:
        if b[i] == a[0]:
            j = i
            k = 0
            while k < len(a):
                if a[j+k]!=b[j]:
                    break
                else:
                    if k == len(a):
                        return True
            i += 1
        else:
            i += 1
    return -1