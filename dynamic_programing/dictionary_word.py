'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
      
def dictionary_word(a,b):
    n = len(a)
    dp = [False for i in range(n+1)]
    dp[0] = True
    for i in range(1,n+1,1):
        for j in range(i):
            if dp[j] and a[j:i] in b:
                dp[i] = True
    return dp[n]

b =set()
b.add("ab")
b.add("b")
b.add("c")
a= "ccabab"

print (dictionary_word(a,b ))
                          