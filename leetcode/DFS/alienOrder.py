###269. Alien Dictionary
#There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
#You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
#Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
#A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.
#Example 1:
#Input: words = ["wrt","wrf","er","ett","rftt"]
#Output: "wertf"
#Example 2:
#Input: words = ["z","x"]
#Output: "zx"
#Example 3:
#Input: words = ["z","x","z"]
#Output: ""
#Explanation: The order is invalid, so return "".
from collections import defaultdict

from caffe2.python.ideep.transform_ideep_net import pairwise


class Solution:
    def alienOrder(self, words):
        return

words = ["wrt","wrf","er","ett","rftt"]
for s, t in pairwise(words):
    print(s,t)
for u,v in zip("wrt", "wrf"):
    print(u,v)

g= {}
g[1] =1
g.setdefault(1,2)
print(g)

s = "asada"
print(s[0:2])

print(iter("aa"))
print(next(iter("adasd")))
it = iter("adasd")
print(next(it))
print(next(it))


class Solution131:
    def countPairs(self, nums, k: int) -> int:
        possible_pair = []
        for i in range(2,k):
            if k % i == 0 and i <= k /i:
                possible_pair.append((i, int(k / i)))
        print(possible_pair)
        num_residule = defaultdict(int)
        for num in nums:
            r = num % k
            num_residule[r] += 1
        print(num_residule)
        n = len(nums)
        cnt = 0
        for x, y in possible_pair:
            if x == y:
                cnt += num_residule[x] * (num_residule[x] - 1) / 2
            else:
                cnt += num_residule[x] * num_residule[y]
        cnt += (num_residule[0] * (n - num_residule[0]))
        cnt += (num_residule[0] * (num_residule[0] - 1) / 2)
        return int(cnt)
s =Solution131()
a=[8,10,2,5,9,6,3,8,2]
b= 6
print(s.countPairs(a,b))




s = "1,3  65  sa"
print(" ".join(s.split()[::-1]))