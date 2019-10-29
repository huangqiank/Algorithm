'''
Created on Sep 28, 2017

@author: qiankunhuang
'''
def all_permutation(array, index ,result):
  # base rule
  if index == len(array):
    print array
    result.append(array)
    return
  
  for i in xrange(0,len(array)-index):
    array[index], array[i] = array[i],array[index]
    all_permutation(array, index + 1, result)
    array[index],array[i] = array[i], array[index]
  return
result = []
all_permutation(['a','b','c'],0,result)
