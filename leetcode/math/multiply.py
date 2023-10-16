##43. Multiply Strings
#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#Example 1:
#Input: num1 = "2", num2 = "3"
#Output: "6"
#Example 2:
#Input: num1 = "123", num2 = "456"
#Output: "56088"


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n =len(num2)
        if n ==0 or m==0 or num1 =="0" or num2 == "0":
            return "0"
        res =[0] * (m + n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                res[i+j+1] += int(num1[i]) * int(num2[j])
        for i in range(m+n-1,0,-1):
            add = res[i] //10
            m =res[i]%10
            res[i-1] += add
            res[i] = m
        if res[0] == 0 :
            index=1
        else:
            index = 0
        return "".join([str(x) for x in res[index:]])


s = "asd   ada   re"
print(s.split(" "))
