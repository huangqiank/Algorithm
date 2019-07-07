'''
Created on Jan 25, 2018

@author: qiankunhuang
'''
# remove string
def remove(s):
    lst=[]
    for i in s:
        if  i != 'u' and i != 'n':
            lst.append(i)
    return ''.join(lst)
# remove stringlist
def remove_listarrsy(s):
    lst = list(s)
    i,j=0,0
    while j < len(lst):
        if lst[j] not in ['n','u']:
            lst[i] = lst[j]
            i+=1
        j+=1
    return lst[:i
               ]

    
    
    
