##264. 丑数 II
##给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#示例 1：

#输入：n = 10
#输出：12
#解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        num_set = set()
        while n >0 :
            num = heapq.heappop(h)
            n-=1
            if num*2 not in num_set:
                heapq.heappush(h,num*2)
                num_set.add(num*2)
            if num*3 not in num_set:
                heapq.heappush(h,num*3)
                num_set.add(num*3)
            if num*5 not in num_set:
                heapq.heappush(h,num*5)
                num_set.add(num*5)
        return num