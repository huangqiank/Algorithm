##Given a string, determine if it is a palindrome,
##considering only alphanumeric characters and ignoring cases.
##Note: For the purpose of this problem,
##we define empty string as valid palindrome.
##Example 1:
##Input: "A man, a plan, a canal: Panama"
##Output: true
##Example 2:
##Input: "race a car"
##Output: false
##出处。

def isPalindrome(s):
    s = filter(str.isalnum, s)
    s = ''.join(list(s))
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < len(s) and j >-1:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    if i != len(s):
        return False
    if j != -1:
        return False
    return True


s = "0P"
print(isPalindrome(s))
