'''
Created on Sep 30, 2017

@author: qiankunhuang
'''
def find_common_number(A,B):
    B=set(B)
    A=set(A)
    res=[]
    for i in A:
        if i in B:
            res.append(i)
    return res
A =[1,1,2,2,3,4]
B=[2,3,5,6]
print find_common_number(A,B)
            
def find_common2(A,B):
    d = set()
    if len(A) <= len(B):
        n = len(A)
        small = A
        large = B
    else:
        n = len(B)
        small = B
        large = A   
    for j in small:
        l = 0
        r = len(large) - 1
        while l + 1 < r:
            mid = (l+r)/2
            if j  == large[mid]:
                d.add(j )
                break
            if j < large[mid]:
                r = mid
            if j > large[mid] :
                l = mid
        if large[l] == j :
            d.add(j)
        if large[r] == j:
            d.add(j)
    return d

def find_common3(A ,B):
    C=set()
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            C.add(A[i])
            i += 1
            j += 1
        if A[i] < B[j]:
            i += 1
        if A[i] > B[j]:
            j += 1
    return C

        
    
    
    
    
        
    
    