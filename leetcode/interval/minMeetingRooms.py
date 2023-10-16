##253. Meeting Rooms II
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        start = []
        end = []
        for i, j in intervals:
            start.append(i)
            end.append(j)
        start = sorted(start)
        end = sorted(end)
        i = 0
        j = 0
        count = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                i += 1
                j += 1
        return count


class Solution:
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals,key = lambda x:x[0])
        res = []
        count = 0
        i = 0
        while i < len(intervals):
            if len(res) == 0:
                count += 1
                res.append(intervals[i][1])
                i += 1
                continue
            if res[0] > intervals[i][0]:
                count += 1
                heapq.heappush(res, intervals[i][1])
            else:
                heapq.heappop(res)
                heapq.heappush(res, intervals[i][1])
            i += 1
        return count

    class Solution:
        def minMeetingRooms(self, intervals: List[List[int]]):
            i = 1
            n = len(intervals)
            intervals = sorted(intervals, key=lambda x: x[0])
            count = 1
            if n == 0:
                return 0
            if n == 1:
                return 1
            res = [intervals[0][1]]
            while i < n:
                if res[0] > intervals[i][0]:
                    heapq.heappush(res, intervals[i][1])
                    count += 1
                else:
                    heapq.heappop(res)
                    heappush(res, intervals[i][1])
                i += 1
            return count


