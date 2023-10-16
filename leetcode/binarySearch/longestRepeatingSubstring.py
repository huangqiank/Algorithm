##1062. Longest Repeating Substring
#Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.
#Example 1:
#Input: s = "abcd"
#Output: 0
#Explanation: There is no repeating substring.
#Example 2:

#Input: s = "abbaba"
#Output: 2
#Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        left = 0
        right = len(s)
        while left + 1<right:
            mid = int((left+right)/2)
            if self.search(s,mid):
                left = mid
            else:
                right = mid
        if self.search(s,right):
            return right
        if self.search(s,left):
            return left

    def search(self,s,l):
        seen = set()
        n = len(s)
        for i in range(n-l+1):
            if s[i:i+l] in seen:
                return True
            seen.add(s[i:i+l])
        return False