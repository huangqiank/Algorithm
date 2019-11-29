##Given two strings S and T, 
# return if they are equal when both are typed into empty text editors.
# means a backspace character.
# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
# Can you solve it in O(N) time and O(1) space?
class Solution:
    def backspaceCompare(self, S: str, T: str):
        i = len(S) - 1
        j = len(T) - 1
        k = 0
        m = 0
        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == "#" or k > 0):
                if S[i] == "#":
                    k += 1
                else:
                    k -= 1
                i -= 1
            while j >= 0 and (T[j] == "#" or m > 0):
                if T[j] == "#":
                    m += 1
                else:
                    m -= 1
                j -= 1
            if i < 0 or j < 0:
                break
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        while i >= 0 and (S[i] == "#" or k > 0):
            if S[i] == "#":
                k += 1
            else:
                k -= 1
            i -= 1
        if i >= 0 and S[i] != "#":
            return False
        while j >= 0 and (T[j] == "#" or m > 0):
            if T[j] == "#":
                m += 1
            else:
                m -= 1
            j -= 1
        if j >= 0 and S[j] != "#":
            return False
        return True


a = "ab##"
b = "c#d#"
s = Solution()
print(s.backspaceCompare(a, b))
