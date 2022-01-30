#91. 解码方法
#一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。
#给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。
#题目数据保证答案肯定是一个 32 位 的整数。
#示例 1：
#输入：s = "12"
#输出：2
#解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#示例 2：
#输入：s = "226"
#输出：3
#解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。


class Solution1489:
    def numDecodings(self, s: str) -> int:
        num_list=[]
        for i in range(11,27):
            num_list.append(str(i))
        num_list.remove("20")
        s= str(s)
        n= len(s)
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
        dp =[0 for i in range(n)]
        for i in range(n):
            if s[i]=="0":
                dp[i]=0
            else:
                dp[i]=1
        if s[0:2] in num_list:
            dp[0]=1
            dp[1]=2
        elif s[1] == "0" and s[0:2] not in ["20", "10"]:
            return 0
        elif s[0:2] in ["20","10"]:
            dp[0]=0
            dp[1]=1
        else:
            dp[0]=1
            dp[1]=1
        ## [1,0,1]
        ## [1,1,0]
        for i in range(2,n):
            if s[i] == "0" and s[i-1:i+1] not in ["20","10"]:
                    return 0
            if s[i-1:i+1] in num_list:
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-1:i+1] =="20" or s[i-1:i+1] =="10":
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]
s= Solution1489()
print(s.numDecodings("06"))