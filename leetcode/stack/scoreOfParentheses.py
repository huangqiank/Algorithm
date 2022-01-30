##856. 括号的分数
# 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
# () 得 1 分。
# AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
# (A) 得 2 * A 分，其中 A 是平衡括号字符串。
# 示例 1：
# 输入： "()"
# 输出： 1
# 示例 2：
# 输入： "(())"
# 输出： 2
# 示例 3：
# 输入： "()()"
# 输出： 2
# 示例 4：
# 输入： "(()(()))"
# 输出： 6
## (( ))
##()()
## (()())
##(())
## ( 2
## 遇到 ） 出
## ( 2 进
## 2,tmp =0 , + 2, 继续出
##


class Solution:
    def scoreOfParentheses(self, s):
        i = 0
        stack = []
        n = len(s)
        while i < n:
            if len(stack) == 0:
                stack.append(s[i])
            elif s[i] == "(":
                stack.append("(")
            elif s[i] == ")":
                ans = stack.pop()
                if ans == "(":
                    stack.append(1)
                else:
                    while len(stack) != 0 and stack[-1] != "(":
                        ans += stack.pop()
                    stack.pop()
                    stack.append(2 * ans)
            i += 1
        return sum(stack)


s = Solution()
print(s.scoreOfParentheses("()()"))

## 2+4
