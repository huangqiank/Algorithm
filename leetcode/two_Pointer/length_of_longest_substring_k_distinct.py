##340. 至多包含 K 个不同字符的最长子串
# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
# 示例 1:
# 输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。
# 示例 2:
# 输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0
        char_dict = {}
        n = len(s)
        max_size = 0
        while right < n:
            char_dict[s[right]] = right
            right += 1
            if len(char_dict) == k + 1:
                del_idx = min(char_dict.values())
                del char_dict[s[del_idx]]
                left = del_idx + 1
            max_size = max(max_size, right - left)
        return max_size


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = 0
        j = 0
        char_dict = {}
        n = len(s)
        tmp = 0
        while i < n and j < n:
            while len(char_dict) <= k and j < n:
                tmp = max(tmp, j - i)
                char_dict[s[j]] = char_dict.get(s[j], 0) + 1
                j += 1
            while len(char_dict) > k and i < n:
                char_dict[s[i]] -= 1
                if char_dict[s[i]] == 0:
                    char_dict.pop(s[i])
                i += 1
        if k >= len(char_dict):
            tmp = max(tmp, j - i)1
        return tmp
