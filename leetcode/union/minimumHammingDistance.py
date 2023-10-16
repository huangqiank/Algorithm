##1722. Minimize Hamming Distance After Swap Operations
#You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.
#The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).
#Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.
#Example 1:
#Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
#Output: 1
#Explanation: source can be transformed the following way:
#- Swap indices 0 and 1: source = [2,1,3,4]
#- Swap indices 2 and 3: source = [2,1,4,3]
##The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
#Example 2:

#Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
#Output: 2
#Explanation: There are no allowed swaps.
#The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
#Example 3:

#Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
#Output: 0


class union:
    def __init__(self, n):
        self.rank = [0 for i in range(n)]
        self.count = 0
        self.parents = [-1 for i in range(n)]

    def add(self, x):
        self.parents[x] = x
        self.count += 1

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.parents[rootx] = rooty
            else:
                self.parents[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        u = union(n)
        for i in range(n):
            u.add(i)
        for x, y in allowedSwaps:
            u.union(x, y)
        for i in range(n):
            u.find(i)
        parents = u.parents
        index_dict = {}
        for i in range(n):
            if parents[i] not in index_dict:
                index_dict[parents[i]] = [i]
            else:
                index_dict[parents[i]].append(i)
        res = 0
        for i in index_dict.keys():
            source_cnt = self.get_count(source, index_dict[i])
            target_cnt = self.get_count(target, index_dict[i])
            res += self.get_dif(source_cnt, target_cnt)
        return res

    def get_count(self, l, indexs):
        count = {}
        for index in indexs:
            if l[index] in count:
                count[l[index]] += 1
            else:
                count[l[index]] = 1
        return count

    def get_dif(self, source_cnt, target_cnt):
        cnt = 0
        for i in target_cnt.keys():
            cnt += max(target_cnt[i] - source_cnt.get(i, 0), 0)
        return cnt


