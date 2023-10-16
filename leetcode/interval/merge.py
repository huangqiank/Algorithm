##56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals,key = lambda x:x[0])
        res = []
        i = 0
        while i < len(intervals):
            if len(res) == 0:
                res.append([intervals[i][0], intervals[i][1]])
                i += 1
                continue
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])

            else:
                res.append([intervals[i][0], intervals[i][1]])
            i += 1
        return res
