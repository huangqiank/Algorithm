##[a,b,c]
## a  b   c
## ba  c
##max = 中间相差的数目-2
from collections import defaultdict


def numMovesStonesII(stones):
    stones = sorted(stones)
    n = len(stones)
    ##全走一遍
    max_step = max(stones[n - 1] - stones[1] + 1 - (n - 1), stones[n - 2] - stones[0] + 1 - (n - 1))
    i = 0
    min_step = float("inf")
    for j in range(len(stones)):
        while stones[j] - stones[i] >= n:
            i += 1
        if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
            ##-1567
            ##-1356
            ##3456
            ##如果只用走一步，则这么做，其他情况需要n - (j - i + 1)
            min_step = min(min_step, 2)
        else:
            min_step = min(min_step, n - (j - i + 1))
    return [min_step, max_step]

stones =[7,4,9]
##5 7 22
print(numMovesStonesII(stones))

p_cnt = defaultdict(int)
s_cnt = defaultdict(int)

class Solution1:
    def findAnagrams(self, s: str, p: str):
        n = len(s)
        m  = len(p)
        p_cnt= defaultdict(int)
        s_cnt =defaultdict(int)
        res= []
        for i in range(m):
            p_cnt[p[i]] +=1
        i = 0
        j = 0
        while j < n:
            s_cnt[s[j]] +=1
            while s_cnt[s[j]] > p_cnt[s[j]]:
                s_cnt[s[i]] -=1
                i+=1
            if s_cnt ==p_cnt:
                res.append(i)
            j+=1
        return res

s = Solution1()
print(s.findAnagrams(
"cbaebabacd",
"abc"))

