# 91. 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。
# 给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。
# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


class Solution1489:
    def numDecodings(self, s: str) -> int:
        num_list = []
        for i in range(11, 27):
            num_list.append(str(i))
        num_list.remove("20")
        s = str(s)
        n = len(s)
        if n == 0:
            return 0
        if s[0] == "0":
            return 0
        if n == 1:
            return 1
        if n == 2:
            if s in num_list:
                return 2
            elif s[1] == "0" and s not in ["20", "10"]:
                return 0
            return 1
        dp = [0 for i in range(n)]
        for i in range(n):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = 1
        if s[0:2] in num_list:
            dp[0] = 1
            dp[1] = 2
        elif s[1] == "0" and s[0:2] not in ["20", "10"]:
            return 0
        elif s[0:2] in ["20", "10"]:
            dp[0] = 0
            dp[1] = 1
        else:
            dp[0] = 1
            dp[1] = 1
        ## [1,0,1]
        ## [1,1,0]
        for i in range(2, n):
            if s[i] == "0" and s[i - 1:i + 1] not in ["20", "10"]:
                return 0
            if s[i - 1:i + 1] in num_list:
                dp[i] = dp[i - 1] + dp[i - 2]
            elif s[i - 1:i + 1] == "20" or s[i - 1:i + 1] == "10":
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[n - 1]


s = Solution1489()
print(s.numDecodings("06"))


##11 12 ...19
## 21 23 24   29

## f[i] = f[i-2] s[i-2] != 0
## f[i] = f[i-1]  s[i] != 0
class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0 for i in range(n)]
        if s[0] == "0":
            return 0
        dp[0] = 1
        if n == 1:
            return 1
        tmp1, tmp2 = 0, 0
        if s[0] != "0" and 0 < int(s[0] + s[1]) <= 26:
            tmp2 = 1
        if s[1] != "0":
            tmp1 = 1
        dp[1] = tmp1 + tmp2
        for i in range(2, n):
            tmp1, tmp2 = 0, 0
            if s[i - 1] != "0" and 0 < int(s[i - 1] + s[i]) <= 26:
                tmp1 = dp[i - 2]
            if s[i] != "0":
                tmp2 = dp[i - 1]
            dp[i] = tmp1 + tmp2
        return dp[n - 1]


###639. Decode Ways II
# message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.
# Given a string s consisting of digits and '*' characters, return the number of ways to decode it.
# Since the answer may be very large, return it modulo 109 + 7.
# Example 1:
# Input: s = "*"
# Output: 9
# Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
# Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
# Hence, there are a total of 9 ways to decode "*".
##[*][*] = 26 + 9* dp[0]
##[1,2][*] =9* dp[0] + (1:19,2:7)
##[*][0,1..] =  if s[i] ==0: 2   if 0< [i] <8 : 9 + 1  if s[i] ==8,9 : 9
##[1][0 1..9] =    if 0<s[i]<10 : 2 if s[i] == 0: 1
## [2] [....]        if 0<s[1]<8:  2   if s[1] == 0 : 1  else: 1
##[3 .... 9 ][...]   if s[1] =="0" :0 else: 1
class Solution:
    def numDecodings(self, s: str):
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [1 for i in range(n)]
        if s[0] == "0":
            return 0
        if s[0] == "*":
            dp[0] = 9
        else:
            dp[0] = 1
        if len(s) == 1:
            return dp[0]

        tmp1, tmp2 = 0, 0

        if s[1] == "*":
            tmp1 = 9 * dp[0]
        elif s[1] != "0":
            tmp1 = dp[0]

        if s[0] == "2" and s[1] == "*":
            tmp2 = 6
        elif s[0] == "2" and int(s[1]) < 7:
            tmp2 = 1
        elif s[0] == "1" and s[1] == "*":
            tmp2 = 9
        elif s[0] == "1" and s[1] != "*":
            tmp2 = 1
        elif s[0] == "*" and s[1] == "*":
            tmp2 = 15
        elif s[0] == "*" and 0 <= int(s[1]) < 7:
            tmp2 = 2
        elif s[0] == "*":
            tmp2 = 1
        dp[1] = tmp1 + tmp2
        for i in range(2, n):
            tmp1, tmp2 = 0, 0
            if s[i] == "0":
                tmp1 = 0
            elif s[i] == "*":
                tmp1 = 9 * dp[i - 1]
            else:
                tmp1 = dp[i - 1]
            if s[i - 1] == "2" and s[i] == "*":
                tmp2 = 6 * dp[i - 2]
            elif s[i - 1] == "2" and int(s[i]) < 7:
                tmp2 = dp[i - 2]
            elif s[i - 1] == "1" and s[i] == "*":
                tmp2 = 9 * dp[i - 2]
            elif s[i - 1] == "1" and s[i] != "*":
                tmp2 = dp[i - 2]
            elif s[i - 1] == "*" and s[i] == "*":
                tmp2 = 15 * dp[i - 2]
            elif s[i - 1] == "*" and 0 <= int(s[i]) < 7:
                tmp2 = 2 * dp[i - 2]
            elif s[i - 1] == "*":
                tmp2 = dp[i - 2]
            dp[i] = tmp1 + tmp2
            dp[i] %= mod
        return dp[n - 1]


s = Solution()
print(s.numDecodings("**"))


class Solution45:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7

        def check1digit(ch: str) -> int:
            if ch == "0":
                return 0
            return 9 if ch == "*" else 1

        def check2digits(c0: str, c1: str) -> int:
            if c0 == c1 == "*":
                return 15
            if c0 == "*":
                return 2 if c1 <= "6" else 1
            if c1 == "*":
                return 9 if c0 == "1" else (6 if c0 == "2" else 0)
            return int(c0 != "0" and int(c0) * 10 + int(c1) <= 26)

        n = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = b * check1digit(s[i - 1])
            if i > 1:
                c += a * check2digits(s[i - 2], s[i - 1])
            c %= mod
            a = b
            b = c

        return c


s = Solution45()
print(s.numDecodings("**"))


## if s[0] == 0 return 0
## if s[0] == * dp[0]= 9
## else: dp[0] = 1
## dp[1]: tmp1+tmp2
# tmp1
##if s[1]==*  tmp1= 9*dp[0]
##if s[1] ==0 0
##else: dp[0]
##tmp2:
##if s[0] == * and s[1]==* 17
##if s[0] = * and s[1]<7 2
##if s[0] = * and s[1] >=7 1
##if s[0] ==1 and s[1]==* 9
##if s[0] ==1 s[1]!= * 1
##if s[0] == 2 s[1]= * 7
##if s[0] == 2 s[1] >= 7 0
##if s[0] ==2 s[1]<7 1


## dp[i] = tmp2 + tmp1
## tmp1 : if s[i] == 0 , 0 if s[i]==*, 9*dp[i-1] else: dp[i-1]
## tmp2:  if s[i-1] == * and s[i] == *  17*dp[i-2]                if s[i-1] == 0,0            #if s[i-1] > 3,0,    if s[i-1] == 1 and s[i]= *   10 *dp[i-2],
#         if s[i-1] == * and s[i] >6  dp[i-2]                                                                   #if s[i-1] == 1 and s[i] != *   dp[i-2],
#         if s[i-1] == *  and  s[i]<7  2*dp[i-2]                                                                  #if s[i-1] == 2 and s[i]==*       7*dp[i-2]
# if s[i-1] == 2 and s[i] > 6  0
# if s[i-1] == 2  and s[i] <= 6 dp[i-2]
class Solution:
    def numDecodings(self, s):
        mod = 10 ** 9 + 7
        if len(s) == 0:
            return 0
        n = len(s)
        dp = [0 for i in range(n)]
        if s[0] == "0":
            return 0
        elif s[0] == "*":
            dp[0] = 9
        else:
            dp[0] = 1
        if n == 1:
            return dp[0]
        tmp1, tmp2 = 0, 0
        if s[1] == "*":
            tmp1 = 9 * dp[0]
        elif s[1] == "0":
            tmp1 = 0
        else:
            tmp1 = dp[0]
        if s[0] == "*" and s[1] == "*":
            tmp2 = 15
        elif s[0] == "*" and int(s[1]) < 7:
            tmp2 = 2
        elif s[0] == "*" and int(s[1]) >= 7:
            tmp2 = 1
        elif s[0] == "1" and s[1] == "*":
            tmp2 = 9
        elif s[0] == "1" and s[1] != "*":
            tmp2 = 1
        elif s[0] == "2" and s[1] == "*":
            tmp2 = 6
        elif s[0] == "2" and int(s[1]) >= 7:
            tmp2 = 0
        elif s[0] == "2" and int(s[1]) < 7:
            tmp2 = 1
        dp[1] = tmp1 + tmp2
        for i in range(2, n):
            tmp1, tmp2 = 0, 0
            if s[i] == "0":
                tmp1 = 0
            elif s[i] == "*":
                tmp1 = 9 * dp[i - 1]
            else:
                tmp1 = dp[i - 1]

            if s[i - 1] == "*" and s[i] == "*":
                tmp2 = 15 * dp[i - 2]
            elif s[i - 1] == "*" and int(s[i]) > 6:
                tmp2 = dp[i - 2]  #
            elif s[i - 1] == "*" and int(s[i]) < 7:
                tmp2 = 2 * dp[i - 2]
            elif s[i - 1] == "0":
                tmp2 = 0
            elif int(s[i - 1]) > 3:
                tmp2 = 0
            elif s[i - 1] == "1" and s[i] == "*":
                tmp2 = 9 * dp[i - 2]
            elif s[i - 1] == "1" and s[i] != "*":
                tmp2 = dp[i - 2]
            elif s[i - 1] == "2" and s[i] == "*":
                tmp2 = 6 * dp[i - 2]
            elif s[i - 1] == "2" and int(s[i]) > 6:
                tmp2 = 0
            elif s[i - 1] == "2" and int(s[i]) <= 6:
                tmp2 = dp[i - 2]
            dp[i] = tmp1 + tmp2
            dp[i] %= mod
        return dp[n-1]
