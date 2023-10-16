'''
Created on Jan 19, 2018

@author: qiankunhuang
'''
from collections import defaultdict


def closest(a, b, c, k):
    matrix = []
    n=len(a)
    for i in range(len(a)):
        for j in range(len(b)):
            d = [[t**2+(a[i])**2+(b[j])**2,(a[i],b[j],t)] for t in c]
            matrix.append(d)
    return k_th( matrix, k)
import heapq
def k_th(matrix,k):
    n =len(matrix)
    res=[]
    for i in range(n):
        heapq.heappush(res,(matrix[i][0][0],matrix[i][0][1],0,matrix[i]))
    for j in range(k-1):
        pair = heapq.heappop(res)
        if pair[2]+1<len(pair[3]):
            heapq.heappush(res,(pair[3][pair[2]+1][0],pair[3][pair[2]+1][1],pair[2]+1,pair[3]))
    return heapq.heappop(res)[1]
A =[1,3,5]
B = [2,4]
C = [3,6]



class Solution(object):
   def kthSmallest(self,matrix,k):
        import heapq
        res=[]
        n=len(matrix)
        for i in range(n):
          heapq.heappush(res,(matrix[i][0][0],matrix[i][0][1],0,matrix[i]))
        for j in range(k-1):
          pair = heapq.heappop(res)
          if pair[2]+1<len(pair[3]):
            heapq.heappush(res,(pair[3][pair[2]+1][0],pair[3][pair[2]+1][1],pair[2]+1,pair[3]))
        return heapq.heappop(res)[1]
   def closest(self, a, b, c, k):
        matrix = []
        for i in range(len(a)):
          for j in range(len(b)):
              d = [[t*t+a[i]*a[i]+b[j]*b[j],(a[i],b[j],t)] for t in c]
              matrix.append(d)
        return self.kthSmallest(matrix,k)


class Solution33:
    def invalidTransactions(self, transactions):
        name_transaction = defaultdict(list)
        for t in transactions:
            name, time, amount, city = t.split(",")
            name_transaction[name].append([time, amount, city])
        res = []
        for name in name_transaction:
            l = name_transaction[name]
            l = sorted(l, key=lambda x: int(x[0]))
            visit = set()
            if name == "bob":
                print(l)
            for i in range(len(l)):
                if int(l[i][1]) > 1000:
                    new = ",".join([name] + l[i])
                    if i not in visit:
                        visit.add(i)
                        res.append(new)
                j = i - 1
                while j >= 0 and int(l[i][0]) - int(l[j][0]) <= 60:
                    if l[i][2] != l[j][2]:
                        new = ",".join([name] + l[i])
                        if i not in visit:
                            visit.add(i)
                            res.append(new)
                        new = ",".join([name] + l[j])
                        if j not in visit:
                            visit.add(j)
                            res.append(new)
                    j -= 1
        return res


class Solution123:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        return self.check(str1, str2)

    def check(self, str1, str2):
        print(str1,str2)
        n = len(str1)
        m = len(str2)
        if m > n:
            str1, str2 = str2, str1
        if m == n:
            if str1 == str2:
                return str1
            return ""
        i = 0
        while i < len(str2):
            if str1[i] == str2[i]:
                i += 1
            break

        if i == 0:
            return ""
        return self.check(str1[i:], str2)
s =Solution123()
print(s.gcdOfStrings("AAAAAAAAA","AAACCC"))
