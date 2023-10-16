##剑指 Offer 41. 数据流中的中位数
#如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
#例如，
#[2,3,4] 的中位数是 3
#[2,3] 的中位数是 (2 + 3) / 2 = 2.5
#设计一个支持以下两种操作的数据结构：
#void addNum(int num) - 从数据流中添加一个整数到数据结构中。
#double findMedian() - 返回目前所有元素的中位数。
#示例 1：
#输入：
#["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
#[[],[1],[2],[],[3],[]]
#输出：[null,null,null,1.50000,null,2.00000]
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        ##minheap
        self.a = []
        ##maxheap
        self.b = []

    def addNum(self, num: int) -> None:
        if len(self.a) == len(self.b):
            heapq.heappush(self.b,-num)
            tmp = - heapq.heappop(self.b)
            heapq.heappush(self.a,tmp)
        else:
            heapq.heappush(self.a,num)
            tmp = -heapq.heappop(self.a)
            heapq.heappush(self.b,tmp)
    def findMedian(self) -> float:
        if len(self.a) == len(self.b):
            return (self.a[0] - self.b[0])/2
        return self.a[0]


class MedianFinder2:
    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if len(self.h1) < len(self.h2):
            heapq.heappush(self.h2, num)
            num = heapq. heappop(self.h2)
            heapq.heappush(self.h1, -num)
        elif len(self.h1) == len(self.h2):
            heapq.heappush(self.h1, -num)
            num = -heapq. heappop(self.h1)
            heapq.heappush(self.h2, num)

    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            return (-self.h1[0] + self.h2[0]) / 2
        else:
            return self.h2[0]


##["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
##[[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
m = MedianFinder2()
m.addNum(-1)
m.addNum(-2)
m.addNum(-3)

m.addNum(-4)
print(m.h1) ##[-3,-4]
print(m.h2) ## [-1,-2]  h2    ## -4 -3 -2 -1
print(m.findMedian())