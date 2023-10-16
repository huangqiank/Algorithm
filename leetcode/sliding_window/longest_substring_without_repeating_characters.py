##Given a string, find the length of the longest substring without repeating characters.
##Example 1:
##Input: "abcabcbb"
##Output: 3
##Explanation: The answer is "abc", with the length of 3.
##Example 2:
##Input: "bbbbb"
##Output: 1
##Explanation: The answer is "b", with the length of 1.
##Example 3:
##Input: "pwwkew"
##Output: 3
##Explanation: The answer is "wke", with the length of 3.
##Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s):
    max_length = 0
    if not s or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    for i in range(len(s)):
        word_set = set()
        j = i
        while j < len(s) and s[j] not in word_set:
            word_set.add(s[j])
            j += 1
        max_length = max(max_length, len(word_set))
    return max_length


print(lengthOfLongestSubstring("abcabcbb"))


def lengthOfLongestSubstring(self, s: str) -> int:
    if not s or len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    res = 0
    r = 0
    l = 0
    word_index = {}
    while r < len(s):
        if s[r] not in word_index:
            word_index[s[r]] = r
            res = max(res, r - l + 1)
        else:
            l = max(word_index[s[r]] + 1, l)
            res = max(res, r - l + 1)
            word_index[s[r]] = r
        r += 1
    return res


## word_index[s[i]] = 0
##



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



