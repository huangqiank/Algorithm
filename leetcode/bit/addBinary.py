##67. 二进制求和
#给你两个二进制字符串，返回它们的和（用二进制表示）。
#输入为 非空 字符串且只包含数字 1 和 0。
#示例 1:
#输入: a = "11", b = "1"
#输出: "100"

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            print(x,y, answer,carry)
            x, y = answer, carry
        return bin(x)[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add =0
        n = len(a)
        m =len(b)
        i,j = n-1,m-1
        res =[]
        while i >= 0  or j >=0 :
            if i>=0:
                s = int(a[i])
            else:
                s = 0
            if j>=0:
                t = int(b[j])
            else:
                t =0
            if s+ t +add == 2:
                res.append("0")
                add =1
            elif s+t + add ==1:
                res.append("1")
                add= 0
            elif s+t + add ==0:
                res.append("0")
                add = 0
            else:
                res.append("1")
                add = 1
            i-=1
            j-=1
        if add == 1:
            res.append("1")
        return "".join(res[::-1])




print(12&4)
##1001  100
##1100

