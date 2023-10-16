# 394. 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
# 示例 1：
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
class Solution:
    def decodeString(self, s):
        res = []
        i = 0
        n = len(s)
        while i < n:
            if "0" <= s[i] <= "9":
                tmp = ""
                while i < n and "0" <= s[i] <= "9":
                    tmp += s[i]
                    i += 1
                res.append(tmp)
            elif "a" <= s[i] <= "z":
                tmp = ""
                while i < n and "a" <= s[i] <= "z":
                    tmp += s[i]
                    i += 1
                res.append(tmp)
            elif s[i] == "[":
                res.append("[")
                i += 1
            elif s[i] == "]":
                tmp = []
                last = res.pop()
                while last != "[":
                    tmp.append(last)
                    last = res.pop()

                num = int(res.pop())
                res.append(num * "".join(tmp[::-1]))
                i += 1
        return "".join(res)


a = ["ada"]
print(a[::-1])
s = Solution()
print(s.decodeString(a))
