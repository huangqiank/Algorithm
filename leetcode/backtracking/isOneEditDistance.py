##161. One Edit Distance
#Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
#A string s is said to be one distance apart from a string t if you can:
#Insert exactly one character into s to get t.Delete exactly one character from s to get t.
#Replace exactly one character of s with a different character to get t.
#Example 1:
#Input: s = "ab", t = "acb"
#Output: true
#Explanation: We can insert 'c' into s to get t.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t)) >1:
            return False
        if len(t) < len(s):
            return self.isOneEditDistance(t,s)
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i+1:] == t[i:] or s[i:]==t[i+1:]
        return len(t) == 1+ len(s)