##395. Longest Substring with At Least K Repeating Characters
# Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.
# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

class Solution:
    def longestSubstring(self, s: str, k: int):
        if len(s) < k:
            return
        s_count = {}
        for i in s:
            if i not in s_count:
                s_count[i] = 1
            else:
                s_count[i] += 1
        ans = -float("inf")
        for i in s_count.keys():
            if s[i] < k:
                l = s.split(s[i])
                for j in l:
                    ans = max(ans,self.longestSubstring(j))
        return len(s)
