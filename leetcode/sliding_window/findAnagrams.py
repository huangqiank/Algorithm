##438. 找到字符串中所有字母异位词
#给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
## 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#示例 1:
#输入: s = "cbaebabacd", p = "abc"
#输出: [0,6]
#解释:
#起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
#起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        m = len(p)
        p_cnt = defaultdict(int)
        s_cnt = defaultdict(int)
        res = []
        for i in range(m):
            p_cnt[p[i]] += 1
        i = 0
        j = 0
        while j < n:
            s_cnt[s[j]] += 1
            while s_cnt[s[j]] > p_cnt[s[j]]:
                s_cnt[s[i]] -= 1
                i += 1
            if s_cnt == p_cnt:
                res.append(i)
            j += 1
        return res

