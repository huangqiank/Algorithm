# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
# 注意:
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
# 示例 1 :
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
## a[i-1] > a[i] 就删除a[i-1]
## 1234
## 4321


class Solution:
    def removeKdigits(self, num, k):
        num = [int(i) for i in num]
        n = len(num)
        res = [num[0]]
        count = 0
        for i in range(1, n):
            while len(res) > 0 and res[-1] > num[i] and count < k:
                res.pop()
                count += 1
            res.append(num[i])
        res = [str(i) for i in res]
        ans = "".join(res).lstrip("0")
        dif = k - count
        if dif > 0 and len(ans) <= dif:
            return 0
        m = len(ans)
        if dif > 0 and m > dif:
            ans = ans[0:m - dif]
        if dif == 0 and len(ans) == 0:
            return 0
        return str(ans)


s = Solution()
print(s.removeKdigits("10", 1))
