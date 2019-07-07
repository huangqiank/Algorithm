'''
Created on Jan 18, 2018

@author: qiankunhuang
'''

def reverse_word(input):
    c=[]
    res=[]
    n =len(input)
    i=0
    while i < n:
        if input[i] != " ":
            c.append(input[i])
            i+=1
        else:
            res.append(c)
            i+=1
            c=[]
    res.append(c)
    res.reverse()
    b = [''.join(i) for i in res] 
    return ' '.join(b)
print  reverse_word('I love Google')
    