'''
Created on Feb 16, 2018

@author: qiankunhuang
'''

def binarysearch(list,k):
    left = 0
    right = len(list)
    while left + 1 < right:
        mid = (left+right)/2
        if list[mid] == k:
            return mid
        if list[mid] < k:
            left=mid
        if  list[mid] > k:
            right=mid
    if abs(list[left]-k) <= abs(list[right]-k):
        return left
    return right
def k_closet(list,x,k):
    index = binarysearch(list,x)
    res=[]
    left = index
    right = index+1
    while left>=0 and right < len(list) and k>0:
        k-=1
        if abs(list[left]-x) <= abs(list[right]-x):
            res.append(list[left])
            left-=1
        else:
            res.append(list[right])
            right+=1
    while k>0 and left>0:
            res.append(list[left])
            left-=1
            k-=1    
    while k>0 and right<len(list):
            res.append(list[right])
            right+=1
            k-=1   
    return res 
print k_closet([1,2,3,4,5,6],2,4)   
        
        
    
            
             
        
        
    
    
         