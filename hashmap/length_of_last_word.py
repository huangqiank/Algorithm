'''
Created on Oct 8, 2017

@author: qiankunhuang
'''
def length_of_last_word(str):
    n=len(str)
    last=0
    while n>0 and str[n-1]==" ":
        n-=1
    while n>0 and str[n-1] !=" ":
        n-=1
        last+=1
    return last
A="abc des fs  "
print length_of_last_word(A)

    