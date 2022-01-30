
##1229. 安排会议日程
# 你是一名行政助理，手里有两位客户的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排合适的会议时间。
# 「会议时间」是两位客户都有空参加，并且持续时间能够满足预计时间 duration 的 最早的时间间隔。
# 如果没有满足要求的会议时间，就请返回一个 空数组。
# 「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。
# 题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。

# 示例 1：
# 输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# 输出：[60,68]
# 示例 2：

# 输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# 输出：[]


class Solution:
    def minAvailableDuration(self, slots1, slots2, duration):
        slots1 = sorted(slots1, key=lambda x: x[0])
        slots2 = sorted(slots2, key=lambda x: x[0])
        i, j = 0, 0
        n = len(slots1)
        m = len(slots2)
        while i < n and j < m:
            a, b, c, d = slots1[i][0], slots1[i][1], slots2[j][0], slots2[j][1]
            begin = max(a, c)
            end = min(b, d)
            res = self.intersect(begin, end, duration)
            if res == 1:
                return [begin, begin + duration]
            if b < c:
                i += 1
            elif a > d:
                j += 1
            elif a <= c <= b<= d:
                i += 1
            elif c <= a <= b <= d:
                i += 1
            elif a <= c <= d <= b:
                j += 1
            elif c <= a <= d <= b:
                j += 1
        return []

    def intersect(self, begin, end, duration):
        if end - begin >= duration:
            return 1
        return -1
