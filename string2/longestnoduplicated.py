'''
Created on Jan 18, 2018

@author: qiankunhuang
'''
def lswrc(s):
    cur_length = 1
    max_length= 1
    n = len(s)
    index = {}
    index[s[0]] = 0
    for i in range(1,n,1):
        if s[i] not in index.keys():
            index[s[i]] = i
            cur_length += 1
        else:
            a = index[s[i]]
            if a+cur_length>=i:
                max_length = max(max_length,cur_length)
                cur_length = i - a
                index[s[i]] = i
            else:
                index[s[i]] = i
                cur_length += 1
    max_length = max(max_length,cur_length)
    return max_length
string = "ABDEFGHBEFA"
length = lswrc(string)
print (length)

def longestNoDuplicateArray(s):
    cur = 1
    maxLength = 1
    n = len(s)
    dic = {}
    dic[s[0]] = 1
    for i in range(1, n, 1):
        if s[i] not in dic.keys():
            dic[s[i]] = i
            cur += 1
        else:
            dic[s[i]] = i
            maxLength = max(maxLength, cur)
            cur = i - dic[s[i]]
    maxLength = max(maxLength, cur)
    return maxLength


string = "ABDBEFGHA"
print(longestNoDuplicateArray(string))

 