###1255 输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# 输出：23
# 解释：
# 字母得分为  a=1, c=9, d=5, g=3, o=2
# 使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。
# 而单词 "dad" 和 "dog" 只能得到 21 分。
# 示例 2：

# 输入：words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# 输出：27
# 解释：
# 字母得分为  a=4, b=4, c=4, x=5, z=10
# 用给定的字母表 letters，我们可以组成单词 "ax" (4+5)， "bx" (4+5) 和 "cx" (4+5) ，总得分为 27 。
# 单词 "xxxz" 的得分仅为 25 。

class Solution:
    def maxScoreWords(self, words, letters, score):
        l = [0 for i in range(26)]
        for i in letters:
            l[ord(i) - ord("a")] += 1
        n = len(words)
        max_score = 0
        for state in range(1 << n):
            tmp = 0
            flag = 1
            need_letter = [0 for i in range(26)]
            for j in range(n):
                if (state >> j) & 1:
                    for s in words[j]:
                        need_letter[ord(s) - ord("a")] += 1
            for i in range(26):
                if need_letter[i] > l[i]:
                    flag = 0
                    break
            if flag == 1:
                for i in range(26):
                    tmp += need_letter[i] * score[i]
            max_score = max(max_score, tmp)
        return max_score
