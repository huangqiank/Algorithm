'''
Created on Jan 25, 2018

@author: qiankunhuang
'''

def remove_duplicates(str):
    if not str or len(str)<2:
        return str
    lst = list(str)
    i,j=0,1
    while j<len(lst):
        if lst[j] != lst[i]:
            lst[i+1] =lst[j]
            i+=1
        j+=1
    return lst[:i+1]
    
def remove_duplicates2(str):
    if not str or len(str)<2:
        return str
    lst = list(str)
    i,j=1,1
    while j<len(lst):
        if lst[j] != lst[i-1]:
            lst[i] =lst[j]
            i+=1
        j+=1
    return lst[:i]