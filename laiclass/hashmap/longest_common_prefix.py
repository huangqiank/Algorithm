'''
Created on Oct 8, 2017

@author: qiankunhuang
'''


def longest_common_prefix(str_list):
    if not str_list:
        return ""
    shortest = min(str_list, key=len)
    ## ab
    for i, ch in enumerate(shortest):
        ## 0 a
        ## 1 b
        for other in str_list:
            if other[i] != ch:
                return shortest[:i]
    return shortest


A = ["abcd", "abcd", "ab"]
print(longest_common_prefix(A))
