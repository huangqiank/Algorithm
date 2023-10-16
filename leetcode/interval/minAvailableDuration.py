##1229. Meeting Scheduler
# Given the availability time slots arrays slots1 and
# slots2 of two people and a meeting duration duration,
# return the earliest time slot that works for both of them and is of duration duration.
# If there is no common time slot that satisfies the requirements,
# return an empty array.
# The format of a time slot is an array of two elements [start, end]
#  representing an inclusive time range from start to end.
# It is guaranteed that no two availability slots of the same person
#  intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person,
# either start1 > end2 or start2 > end1.
# Example 1:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]

class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        slots2 = sorted(slots2, key=lambda x: x[0])
        slots1 = sorted(slots1, key=lambda x: x[0])
        i = 0
        j = 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] <= slots2[j][0]:
                i += 1
                continue
            if slots2[j][1] <= slots1[i][0]:
                j += 1
                continue
            if duration <= (min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0])):
                tmp = max(slots1[i][0], slots2[j][0])
                return [tmp, tmp + duration]
            if slots1[i][1] > slots2[j][0]:
                if slots1[i][1] < slots2[j][1]:
                    i += 1
                else:
                    j += 1
                continue
            if slots2[j][1] > slots1[i][0]:
                if slots2[j][1] < slots1[i][1]:
                    j += 1
                else:
                    i += 1
                continue
        return []


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])
        i = 0
        j = 0
        while i < len(slots1) and j < len(slots2):
            a, b = slots1[i]
            c, d = slots2[j]
            if b <= c:
                i += 1
                continue
            if d <= a:
                j += 1
                continue
            #           -------
            #           a  c b  d   (a,b)+=1
            #           a c d b     (c,d) +=1
            #           c a b d    (a,b) +=1
            ##          c a d  b    (c,d) +=1

            if min(d, b) - max(a, c) >= duration:
                return [max(a, c), min(min(d, b), max(a, c) + duration)]
            if d < b:
                j += 1
            else:
                i += 1
        return []

