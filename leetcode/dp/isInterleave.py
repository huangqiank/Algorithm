##97. 交错字符串
#给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
#两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
#s = s1 + s2 + ... + sn
#t = t1 + t2 + ... + tm
#|n - m| <= 1
#交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
#提示：a + b 意味着字符串 a 和 b 连接。
#示例 1：
#输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#输出：true
## 可以相交
## 整体往后移一位

class Solution:
    def isInterleave(self, s1, s2, s3):
        l = len(s1)
        m = len(s2)
        x = len(s3)
        ##0 01  012
        ## 12  3
        ## L*M
        ## s1[i] == s3[i+j-1], f(i,j)= f(i,j-1)
        ## s2[j] == s3[i+j-1], f(i,j) = f(i-
        if l+m != x:
            return False
        dp = [[0 for j in range(m)] for i in range(l)]
        dp[0][0]=1
        for i in range(l+1):
            for j in range(m+1):
                if i>0:
                    if s1[i-1] == s3[i+j-1]:
                        dp[i][j] = max(dp[i][j],dp[i-1][j])
                if j >0 :
                    if s2[j-1] == s3[i+j-1]:
                        dp[i][j] =max(dp[i][j],dp[i][j-1])
        return dp[l][m]==1



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False
        dp = [[0 for i in range(m)] for j in range(n)]
        if n == 0:
            return s2 == s3
        if m == 0:
            return s1 == s3
        if (s1[0] + s2[0] == s3[:2]) or (s2[0] + s1[0] == s3[:2]):
            dp[0][0] = 1
        for j in range(1, m):
            if s1[0] == s3[j + 1] and s2[:j + 1] == s3[:j + 1]:
                dp[0][j] = 1
            if s2[j] == s3[j + 1]:
                dp[0][j] = max(dp[0][j - 1], dp[0][j])
        for j in range(1, n):
            if s2[0] == s3[j + 1] and s1[:j + 1] == s3[:j + 1]:
                dp[j][0] = 1
            if s1[j] == s3[j + 1]:
                dp[j][0] = max(dp[j - 1][0], dp[j][0])
        for i in range(1, n):
            for j in range(1, m):
                if s1[i] == s3[i + j + 1] and dp[i - 1][j]:
                    dp[i][j] = 1
                if s2[j] == s3[i + j + 1] and dp[i][j - 1]:
                    dp[i][j] = 1
        print(dp)
        return dp[n - 1][m - 1] == 1




