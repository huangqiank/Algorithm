##编写一个 StockSpanner 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。
# 今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。
# 例如，如果未来7天股票的价格是 [100, 80, 60, 70, 60, 75, 85]，那么股票跨度将是 [1, 1, 1, 2, 1, 4, 6]。

# ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# 输出：[null,1,1,1,2,1,4,6]
# [(100,1),(80,1),75(4),]
class StockSpanner:
    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        if len(self.s) == 0:
            self.s.append((price, 1))
            return 1
        tmp = 0
        while len(self.s) != 0 and self.s[-1][0] <= price:
            pre_price, count = self.s.pop()
            tmp += count
        self.s.append((price, 1 + tmp))

        return 1 + tmp