##Given an array of meeting time intervals
##consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
##find the minimum number of conference rooms required.
##Example 1:
##Input: [[0, 30],[5, 10],[15, 20]]
##Output: 2
##Example 2:
##Input: [[7,10],[2,4]]
##Output: 1
##计算相交个数，相交一次加一个，取max
##在遇到开始时间比上一个结束时间晚的的时候,pop 出去。


import heapq


def minMeetingRooms(intervals):
    if not intervals or len(intervals) == 0:
        return 0
    intervals = sorted(intervals, key=lambda interval: (interval[0], interval[1]))
    res = [] ##存截止时间
    count = 0
    for i in range(len(intervals)):
        if len(res) == 0:
            res.append(intervals[i][1])
            count += 1
            continue
        last = res[0]
        if last > intervals[i][0]:
            count += 1
            heapq.heappush(res, intervals[i][1])
        else:
            ## 如果大于 就可以空出一间房间， 让新的meeting 开始
            heapq.heappop(res)
            heapq.heappush(res, intervals[i][1])
    return count


intervals = [[13, 15], [1, 13]]
print(minMeetingRooms(intervals))
intervals = [[10, 11], [4, 9], [4, 17], [11, 13], [14, 15]]
print(minMeetingRooms(intervals))
intervals = [[0, 3], [1, 4], [2, 5], [3, 6]]
print(minMeetingRooms(intervals))

[4,5,6]
