##给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
# 示例 1：
# 输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# 输出：[1,0,0,0,0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
# 示例 2：
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]
# 示例 3：
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]


class Solution:
    def addNegabinary(self, arr1, arr2):
        n = max(len(arr1), len(arr2)) + 2
        res = []
        carry = 0
        arr1 = [0] * (n - len(arr1)) + arr1
        arr2 = [0] * (n - len(arr2)) + arr2
        for i in range(n - 1, -1, -1):
            l1 = arr1[i]
            l2 = arr2[i]
            cur = l1 + l2 + carry
            if cur == -1:
                cur = 1
                carry = 1
            elif cur == 2:
                cur = 0
                carry = -1
            elif cur == 3:
                cur = 1
                carry = -1
            else:
                carry = 0
            res.append(cur)
        ## 去掉尾部的0
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]




print(int(1/(-2)))
print(int(1%(-2)))
## 1 ---> 1
# 0   ---> 0
# -1    ---> 1 carry = 1
# 2 --->0  carry = -1
# [1] +[1] + [1] =3
arr1 = [0]
arr2 = [0]
# [1,0,0,0,0]

s = Solution()
#print(s.addNegabinary(arr1, arr2))
