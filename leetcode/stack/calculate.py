##227. 基本计算器 II
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 整数除法仅保留整数部分。
# 示例 1：
# 输入：s = "3+2*2"
# 输出：7
##示例 1：
# 输入：s = "3+2*2"
# 输出：7
# 示例 2：
# 输入：s = " 3/2 "
# 输出：1
# 示例 3：
# 输入：s = " 3+5 / 2 "
# 输出：5
## operator = ["+","*"]
##  num = [int1,int2]
## "+-"
## "*/+-"


class Solution:
    def calculate(self, s):
        n = len(s)
        tmp = ""
        pre = "+"
        res = []
        for i in range(n):
            if s[i].isdigit():
                tmp += s[i]
            if s[i] in "+-*/":
                if pre == "+":
                    res.append(int(tmp))
                if pre == "-":
                    res.append(-int(tmp))
                if pre == "*":
                    last = res.pop()
                    res.append(int(tmp) * last)
                if pre == "/":
                    last = res.pop()
                    res.append(int(last / int(tmp)))
                tmp = ""
                pre = s[i]

        if pre == "+":
            res.append(int(tmp))
        if pre == "-":
            res.append(-int(tmp))
        if pre == "*":
            last = res.pop()
            res.append(int(tmp) * last)
        if pre == "/":
            last = res.pop()
            res.append(int(last / int(tmp)))
        return sum(res)



class Solution():
    def minTaps(self,n, ranges) :
        prev = [x for x in range(n + 1)]
        for i in range(n + 1):
            l = max(i - ranges[i], 0)
            r = min(i + ranges[i], n)
            prev[r] = min(prev[r], l)

        breakpoint, furthest = n, 2 ** 30
        ans = 0
        for i in range(n, 0, -1):
            furthest = min(furthest, prev[i])
            if i == breakpoint:
                if furthest >= i:
                    return -1
                breakpoint = furthest
                ans += 1
        return ans
s=Solution()
print(s.minTaps(4,[4,2,0,0,0]))




## the example is wrong :
## for postion 2: locations[2] = max(2 - 2,1) to min(1 + 2,3)
##  should be locations[2] = max(2 - 2,1) to min(2 + 2,3)
## the test is also wrong:
## [4,2,0,0,0] only the fountain at position 1 needs to be activated.


def fountainActivation1(n, locations):
    prev = [i for i in range(n)]
    for i in range(n):
        l = max(i - locations[i], 0)
        r = min(i + locations[i], n - 1)
        prev[r] = min(prev[r], l)
    breakpoint, max_value = n - 1, float("inf")
    ans = 0
    for i in range(n - 1, 0, -1):
        max_value = min(max_value, prev[i])
        if i == breakpoint:
            if max_value >= i:
                return -1
            breakpoint = max_value
            ans += 1
    return ans


def fountainActivation(locations):
    # Write your code here
    n = len(locations)
    prev = [i for i in range(n)]
    for i in range(n):
        l = max(i - locations[i], 0)
        r = min(i + locations[i], n - 1)
        prev[r] = min(prev[r], l)
    breakpoint, max_value = n - 1, float("inf")
    ans = 0
    for i in range(n - 1, 0, -1):
        max_value = min(max_value, prev[i])
        if i == breakpoint:
            if max_value >= i:
                return -1
            breakpoint = max_value
            ans += 1
    return ans




##
# Python3 program to implement
# the above appraoch

# Function to find minimum
# number of fountains to be
# activated


