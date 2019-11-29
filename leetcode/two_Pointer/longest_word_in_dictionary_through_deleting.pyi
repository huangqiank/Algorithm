##Given a string and a string dictionary,
##find the longest string in the dictionary
##that can be formed by deleting some characters of the given string.
##If there are more than one possible results,
##return the longest word with the smallest lexicographical order.
##If there is no possible result, return the empty string.
##Example 1:
##Input:
##s = "abpcplea", d = ["ale","apple","monkey","plea"]
##Output:
##"apple"
##Example 2:
##Input:
##s = "abpcplea", d = ["a","b","c"]
##Output:
##"a"
##Note:
##All the strings in the input will only contain lower-case letters.
##The size of the dictionary won't exceed 1,000.
##The length of all the strings in the input won't exceed 1,000.

class Solution:
    def findLongestWord(self, s: str, d) -> str:
        d = sorted(d, key=lambda x: (-len(x), x))
        for word in d:
            if self.check(s, word):
                return word
        return ""

    def check(self, s, word):
        j = 0
        for i in range(len(word)):
            k = s.find(word[i], j)
            if k == -1:
                return False
            j = k + 1
        return True
