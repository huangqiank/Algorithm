##399. Evaluate Division
#You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#Example 1:
#Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
#Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
from itertools import accumulate

class Union:
    def __init__(self):
        self.parent = {}
        self.value = {}
    def add(self,x):
        self.parent[x] = x
        self.value[x] = 1
    def find(self,x):
        if self.parent[x] != x:
            tmp =  self.parent[x]
            self.parent[x] = self.find(tmp)
            self.value[x] *= self.value[tmp]
        return self.parent[x]
    def merge(self,x,y,val):
        rootx = self.find(x)
        rooty = self.find(y)
        ## x/y = val
        ## val[x] =x/rx
        ## val[y] = y/ry
        ## val * val[y] = x/ry
        ##  rx/ry =
        if rootx != rooty :
            self.parent[rootx] = rooty
            self.value[rootx] = self.value[y]*val /self.value[x]
        return

    def is_connected (self,x,y):
        if x not  in self.value or y  not in self.value:
            return -1
        if self.find(x) == self.find(y):
            return 1
        return -1

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        u = Union()
        for (a,b),val in zip(equations,values):
            if a not in u.parent:
                u.add(a)
            if b not in u.parent:
                u.add(b)
            u.merge(a,b,val)
        res =[]
        for i,(a,b) in enumerate(queries):
            if u.is_connected(a,b) != -1:
                res.append(u.value[a]/ u.value[b])
            else:
                res.append(-1.0)
        return res