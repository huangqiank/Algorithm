'''
Created on Jan 22, 2018

@author: qiankunhuang
'''



def quick(list):
    p=0
    q= len(list)-1
    help(list,p,q)
    return list
def help(list,p,q):
    if p<q:
        t = partition(list,p,q)
        help(list,t+1,q)
        help(list,p,t-1)
    return list
def partition(a,p,q):
    left = p-1
    i = p
    while i<q:
        if a[p]<a[q]:
            left+=1
            a[left],a[p] = a[p],a[left]
            i+=1
        else:
            i+=1
    left+=1
    a[left],a[q] = a[q],a[left]
    return left
a=[0,10,2,3,8,5,-1]
print quick(a)


            
        
    
    
    
    
            
        
    
     
        
        

                
                
        
    
    
            
 