##731. 我的日程安排表 II
##实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
# myCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，即 [start, end), 实数 x 的范围为，  start <= x < end。
# 当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
# 每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。否则，返回 false 并且不要将该日程安排添加到日历中。
# 请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)


class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start, end):
        for i, j in self.overlap:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlap.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
        ##  (s1,e1)  (s2,e2)


##  e2 <= s1  or s2 >=e1  no intersect
m = MyCalendarTwo()

print(m.book(10, 20))
print(m.book(50, 60))
print(m.book(10, 40))
print(m.book(5, 15))
print(m.book(5, 10))
print(m.book(25, 55))
