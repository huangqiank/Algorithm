'''
Created on Jan 27, 2018

@author: qiankunhuang
'''
def nearest_entry(arr):
    word_ind = {}
    dist = len(arr)
    for i in range(len(arr)):
        if arr[i] in word_ind:
            dist = max(dist, i - word_ind[arr[i]])
        word_ind[arr[i]] = i
    return dist


a = 'abcdeff'
print(nearest_entry(a))
