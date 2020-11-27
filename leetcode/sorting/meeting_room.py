##Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

##Input: [[0,30],[5,10],[15,20]]
##Output: false
##Example 2:

##Input: [[7,10],[2,4]]
##Output: true


def canAttendMeetings(intervals):
    intervals = sorted(intervals, key=lambda key : (key[0],key[1]))
    for i in range(len(intervals)-1):
##        if intervals[i][1] >=  intervals[i+1][1]:
##            return False
        if intervals[i][1] >= intervals[i+1][0]:
            return False
    return True

intervals = [[7,10],[2,4]]
print(canAttendMeetings(intervals))