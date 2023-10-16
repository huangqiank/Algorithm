# 以字符串的形式给出 n , 以字符串的形式返回 n 的最小 好进制  。
# 如果 n 的  k(k>=2) 进制数的所有数位全为1，则称 k(k>=2) 是 n 的一个 好进制 。
# 示例 1：
# 输入：n = "13"
# 输出："3"
# 解释：13 的 3 进制是 111。
# 示例 2：
# 输入：n = "4681"
# 输出："8"
# 解释：4681 的 8 进制是 11111。
# 示例 3：
# 输入：n = "1000000000000000000"
# 输出："999999999999999999"
# 解释：1000000000000000000 的 999999999999999999 进制是 11。

import math


class Solution:
    def smallestGoodBase(self, n):
        n = int(n)
        m = int(math.log(n, 2))
        ## n = q**0 + q**1 + *** + q**m
        ## (q+1)**m > n  > q**m
        ## q+ 1 > pow(n,1/m) > q
        ## q = pow(n,1/m)
        ## (q**m -1)//q- 1 == n
        for i in range(m, 0, -1):
            q = int(math.pow(n, 1 / i))
            total = 0
            for j in range(i+1):
                total += q ** j
            if total == n:
                return str(q)
        return str(n - 1)

a = [1,2,3,4]
print(a.pop())
print(a)


