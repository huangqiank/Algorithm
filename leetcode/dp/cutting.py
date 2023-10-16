##700 · 杆子分割
#给一个 n 英寸长的杆子和一个包含所有小于 n 的尺寸的价格. 确定通过切割杆并销售碎片可获得的最大值.
#输入：
#[1, 5, 8, 9, 10, 17, 17, 20]
#8
#输出：22
#解释：
#长度    | 1   2   3   4   5   6   7   8
#--------------------------------------------
#价格    | 1   5   8   9  10  17  17  20
#切成长度为 2 和 6 的两段。

from typing import (
    List,
)

class Solution:
    """
    @param prices: the prices
    @param n: the length of rod
    @return: the max value
    """
    def cutting(self, prices: List[int], n: int) -> int:
        l_v = {index+1:x for index,x in enumerate(prices)}
        dp = [0 for i in range(n+1)]
        dp[0]= 0
        for i in range(1,n+1):
            tmp = -float("inf")
            for j in range(1,i+1):
                tmp = max(tmp,dp[i-j] + l_v[j])
            dp[i] = tmp
        return dp[-1]