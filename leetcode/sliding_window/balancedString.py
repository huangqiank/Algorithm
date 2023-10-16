##1234. 替换子串得到平衡字符串
#有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
#假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
#给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。
#你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
#请返回待替换子串的最小可能长度。
#如果原字符串自身就是一个平衡字符串，则返回 0。
#示例 1：
#输入：s = "QWER"
#输出：0
#解释：s 已经是平衡的了。

class Solution:
    def balancedString(self, s: str) -> int:
        word_cnt = defaultdict(int)
        n = len(s)
        m = n/4
        for i in range(n):
            word_cnt[s[i]] +=1
        if word_cnt["Q"]==m and  word_cnt["W"]==m and  word_cnt["R"]==m and  word_cnt["E"]==m:
            return 0
        i,j=0,0
        res = float("inf")
        while j<n:
            word_cnt[s[j]]-=1
            while i< n and word_cnt["Q"]<=m and  word_cnt["W"]<=m and  word_cnt["R"]<=m and  word_cnt["E"]<=m:
                res = min(res,j-i+1)
                word_cnt[s[i]]+=1
                i+=1
            j+=1
        return res
