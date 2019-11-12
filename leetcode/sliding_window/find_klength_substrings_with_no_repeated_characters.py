##Given a string S, return the number of substrings of length K with no repeated characters.
##Example 1:
##Input: S = "havefunonleetcode", K = 5
##Output: 6
##Explanation:
##There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

##Example 2:
##Input: S = "home", K = 5
##Output: 0
##Explanation:
##Notice K can be larger than the length of S. In this case is not possible to find any substring.
##Note:
##1 <= S.length <= 10^4
##All characters of S are lowercase English letters.
##1 <= K <= 10^4


def numKLenSubstrNoRepeats(S, K):
    if len(S) < K:
        return 0
    if not S:
        return 0
    l = 0
    word_dict = {}
    res = []
    for r in range(len(S)):
        if S[r] not in word_dict:
            word_dict[S[r]] = r
        else:
            new_l = word_dict[S[r]]
            for i in range(l, word_dict[S[r]] + 1, 1):
                del word_dict[S[i]]
            word_dict[S[r]] = r
            l = new_l + 1
        while r - l + 1 > K:
            del word_dict[S[l]]
            l += 1
        if len(word_dict) == K:
            res.append("".join(word_dict.keys()))
    return len(res)


print(numKLenSubstrNoRepeats("abab", 2))


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K > len(S) or len(S) == 0:
            return 0
        count = 0
        for p in range(0, len(S) - K + 1):
            c = S[p:p+K]
            p = []
            F = True
            for i in c:
                if i in p:
                    F = False
                    continue
                p.append(i)
            if F: count += 1
        return count


