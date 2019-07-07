'''
Created on Oct 9, 2017

@author: qiankunhuang
'''
      
def dictionary_word2(input,dict):
    word_set=set(dict)
    n=len(input)
    M=[False for i in xrange(0,n+1,1)] 
    M[0]=True
    for i in xrange(1,n+1,1):
        for j in xrange(i):
            if M[j] and input[j:i] in word_set :
                M[i]=True
                break
    return M[n]





print dictionary_word2("adf da","acafafadf")








def dict(A,B):
    c=set(B)
    n=len(A)
    dp = [False for i in xrange(0,n+1,1)]
    dp[0] = True
    for i in xrange(1,n+1,1) :
        for j in xrange(i):
            if A[j:i] in B and dp[j] is True:
                dp[i] = True
                break
    return dp[-1]
                          