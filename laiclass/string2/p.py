'''
Created on Nov 4, 2017

@author: qiankunhuang
'''
def reverse(s):
    l=0
    n=len(s)
    res=[]
    while l<n:
        c=[]
        while l<n and s[l]!=" ":
            c.append(s[l])
            l+=1
        c.reverse()
        if len(res)!=0:
            res.append(" ")
        res.extend(c)
        l+=1
    return "".join(res)
def anagram(a,b):
    if not a and not b and len(a) == 0 and len(b) == 0:
        return
    A={}
    B={}
    for  i in a:
        if i not in A:
            A[i] = 1
        else:
            A[i] += 1
    for j in b:
        if j not in B:
            B[j] = 1
        else:
            B[j] += 1
    if A == B:
        return True
    return False
def f(s,l):
    n = len(s)
    m = len(l)
    res=[]
    if not s or len(s) == 0:
        return s
    if not l or len(l) == 0:
        return res
    for i in range(0,n-m+1,1):
        if anagram(s[i:i+m],l):
            res.append(i)
    return res
print f('ababacbbaac', 'aab')

a=[1,2,3]
a.reverse()
print a
def f1(input):
    if input is None or len(input) == 0:
        return input
    vowel =['a','e','i','o','u']
    n =len(input)
    index=[]
    res=[]
    for i in range(0,n,1):
        if input[i] in vowel:
            index.append(i)
    if len(index)==0 or index is None:
        return ''.join(res)
    for i in input:
        res.append(i)
    old = index[:len(index)/2]
    new = index[len(index)-1:len(index)/2-1:-1]
    for i in range(len(old)):
            res[old[i]],res[new[i]] =res[new[i]],res[old[i]]
    return ''.join(res)
print  f1('awriou')    
a=[1,2,3,4,5,6,7]
print a[:len(a)/2],a[len(a)-1:len(a)/2-1:-1]
print a[-2]
print range(3,3,1)
