# 76. 最小覆盖子串
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str):
        t_dict = {}
        n, m = len(s), len(t)
        word_set = set()
        for i in range(m):
            word_set.add(t[i])
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        if n < m:
            return ""
        s_dict = defaultdict(int)
        if len(s) < len(t):
            return ""
        i, j, l, begin,res = 0, 0, float("inf"), "",""
        while j < n:
            while j < n and s[j] not in word_set:
                j += 1
            if j >= n:
               return res
            s_dict[s[j]] += 1
            flag = 0
            for word in word_set:
                if s_dict[word] < t_dict[word]:
                    flag = 1
                    break
            if flag == 0:
                while i < n and (s[i] not in word_set or s_dict[s[i]] > t_dict[s[i]]):
                    if s[i] in word_set:
                        s_dict[s[i]] -= 1
                    i += 1
                if l > j - i + 1:
                    l = j - i + 1
                    begin = i
                    res = s[begin:begin + l]
            j += 1
        return res


s = "a"
t = "b"
s1 = Solution()
print(s1.minWindow(s, t))
