'''
Created on Feb 15, 2018

@author: qiankunhuang
'''
def reverse(input):
    res=[]
    i = 0
    new=[]
    n = len(input)
    while i < n:
        new=[]
        while i<n and (len(new)== 0 or input[i]!=" "):
            new.append(input[i])
            i+=1
        new = new[::-1]
        res.extend(new)
        res.append(" ")
    return ''.join(res)
S="abc de fg"
print reverse(S)

            
            
        
        
    
     
    
            
            
            
            