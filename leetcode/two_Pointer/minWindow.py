##76. 最小覆盖子串
#给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#注意：

#对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
#如果 s 中存在这样的子串，我们保证它是唯一的答案。
#示例 1：

#输入：s = "ADOBECODEBANC", t = "ABC"
#输出："BANC"

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        word_cnt = {}
        for i in t:
            word_cnt[i] = word_cnt.get(i,0)+1
        i = 0
        j = 0
        ans= ""
        tmp ={}
        n = len(s)
        while j<len(s):
            while j<n and self.check(tmp,word_cnt) == 0:
                tmp[s[j]]=tmp.get(s[j],0)+1
                j+=1
            while self.check(tmp,word_cnt) == 1:
                if ans == "":
                    ans = s[i:j]
                elif j-i <len(ans):
                    ans = s[i:j]
                tmp[s[i]] -=1
                i+=1
        return ans

    def check(self,tmp,word_cnt):
        flag =1
        for i in word_cnt.keys():
            if tmp.get(i,0) < word_cnt[i]:
                flag = 0
                break
        return flag