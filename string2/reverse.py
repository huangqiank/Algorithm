'''
Created on Oct 2, 2017

@author: qiankunhuang
'''
def reverse(S):
    res=[]
    i = 0
    while i < len(S):
        c=[]
        while i<len(S) and S[i] != " ":
            c.append(S[i])
            i+=1
        c.reverse()
        if len(res)!=0:
            res.append(" ")
        res.extend(c)
        i+=1
    return "".join(res)
S="abc de fg"
print reverse(S)

def reverse2(input):
    res=[]
    c=[]
    i = 0
    n = len(input)
    while  i < n :
        if input[i]!=' ':
            c.append(input[i])
            i+=1
        else:
            c.reverse()
            res.extend(c)
            res.append(' ')
            c= []
            i+=1
    return ''.join(res)
print reverse2(S)       
        
            
         
            