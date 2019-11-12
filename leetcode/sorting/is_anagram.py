##Given two strings s and t , write a function to determine if t is an anagram of s.

##Example 1:

##Input: s = "anagram", t = "nagaram"
##Output: true
##Example 2:
##Input: s = "rat", t = "car"
##Output: false

def is_anagram(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] not in s_dict:
            s_dict[s[i]] = 1
        else:
            s_dict[s[i]] += 1
    for i in range(len(t)):
        if t[i] not in t_dict:
            t_dict[t[i]] = 1
        else:
            t_dict[t[i]] += 1

    return s_dict == t_dict
s = "a"
t = "ab"
print()