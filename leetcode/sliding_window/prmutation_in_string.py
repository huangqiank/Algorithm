##Given two strings s1 and s2, write a function to return true if s2
##contains the permutation of s1. In other words,
##one of the first string's permutations is the substring of the second string.
##Example 1:
##Input: s1 = "ab" s2 = "eidbaooo"
##Output: True
##Explanation: s2 contains one permutation of s1 ("ba").
##Example 2:
##Input:s1= "ab" s2 = "eidboaoo"
##Output: False
##Note:
##The input strings only contain lower case letters.
##The length of both given strings is in range [1, 10,000].
def checkInclusion(s1, s2):
    if not s1 and not s2:
        return True
    if not s1 or not s2:
        return False
    word_set = {}
    word_set2 = {}
    l = 0
    length = len(s1)
    for i in range(len(s1)):
        word_set[s1[i]] = word_set.get(s1[i], 0) + 1
    for r in range(len(s2)):
        word_set2[s2[r]] = word_set2.get(s2[r], 0) + 1
        while r - l + 1 > length:
            word_set2[s2[l]] -= 1
            if word_set2[s2[l]] == 0:
                word_set2.pop(s2[l])
            l += 1
        if r - l + 1 == length and word_set2 == word_set:
            return True
    return False


"ooolleoooleh"
print(checkInclusion("ab", "ab"))
