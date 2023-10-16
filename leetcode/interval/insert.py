##57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]


class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        res = []
        while i < n:
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i += 1
                continue
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                while i < n:
                    res.append(intervals[i])
                    i += 1
                return res
            newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]
            i += 1

        if newInterval != [-1, -1]:
            res.append(newInterval)
        return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        i = 0
        n  = len(intervals)
        if n == 0:
            return [newInterval]
        while i < n :
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                i+=1
                continue
            if newInterval[1]< intervals[i][0]:
                res.append(newInterval)
                while i <n :
                    res.append(intervals[i])
                    i+=1
                return res
            newInterval = [min(intervals[i][0],newInterval[0]), max(intervals[i][1], newInterval[1])]
            i+=1
        if len(res) == 0 :
            res.append(newInterval)
            return res
        if res[-1][1] < newInterval[0]:
            res.append(newInterval)
        return res