##Write a function that takes a string as input and reverse only the vowels of a string.
##Example 1:
##Input: "hello"
##Output: "holle"
##Example 2:

##Input: "leetcode"
##Output: "leotcede"
##Note:
##The vowels does not include the letter "y".

class Solution:
    def reverseVowels(self, s):
        s = [s[i] for i in range(len(s))]
        vowels = set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        vowels.add('A')
        vowels.add('U')
        vowels.add('E')
        vowels.add('I')
        vowels.add('O')
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            if i < j:
                if s[i] in vowels and s[j] in vowels:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
        return "".join(s)
a = "hello"
s= Solution()
print(s.reverseVowels(a))