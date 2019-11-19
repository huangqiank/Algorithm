##Implement strStr().
##Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
##Example 1:
##Input: haystack = "hello", needle = "ll"
##Output: 2
##Example 2:
##Input: haystack = "aaaaa", needle = "bba"
##Output: -1
##Clarification:
##What should we return when needle is an empty string? This is a great question to ask during an interview.
##For the purpose of this problem, we will return 0 when needle is an empty string.
##This is consistent to C's strstr() and Java's indexOf().

def strStr(haystack, needle):
    m = len(needle)
    n = len(haystack)
    if m > n:
        return -1
    if m == 0:
        return 0
    j = 0
    while j < n - m + 1:
        if haystack[j:j + m] ==needle :
            return j
        j+=1
    return -1


haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))
