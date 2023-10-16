##986. Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
# Example 1:

# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

class Solution:
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)
        res = []
        while i < n and j < m:
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
            if secondList[j][1] < firstList[i][0]:
                j += 1
                continue
            res.append([max(firstList[i][0], secondList[j][0]), min(secondList[j][1], firstList[i][1])])
            if firstList[i][1] < secondList[j][1]:
                i+=1
                continue
            if secondList[j][1] < firstList[i][1]:
                j+=1
                continue
            if firstList[i][1] == secondList[j][1]:
                i+=1
                j+=1
        return res





    def intersect(self, a, b):
        if a[1] >= b[0] and b[1] >= a[0]:
            return 1
        return 0

    class Solution:
        def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
            i = 0
            j = 0
            n = len(firstList)
            m = len(secondList)
            res = []
            if n == 0 or m == 0:
                return res
            while i < n and j < m:
                a, b = firstList[i]
                c, d = secondList[j]
                if b < c:
                    i += 1
                    continue
                if d < a:
                    j += 1
                    continue
                res.append([max(a, c), min(b, d)])
                if b < d:
                    i += 1
                else:
                    j += 1
            return res
