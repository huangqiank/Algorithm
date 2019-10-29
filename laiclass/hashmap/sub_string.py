'''
Created on Sep 30, 2017

@author: qiankunhuang
'''
def sub_string(A, B):
    if len(A) < len(B):
        min = A
        max = B
    else:
        min = B
        max = A
    for j in xrange(0, len(max) - len(min) + 1, 1):
        if max[j] == min[0]:
            for i in xrange(1, len(min), 1):
                if max[j + i] != min[i]:
                    break
                else:
                    if i == len(min)-1:
                        return True
    return False


print sub_string("abcde", "dabcdfef")
   
print sub_string("abc" , "dabc")


    