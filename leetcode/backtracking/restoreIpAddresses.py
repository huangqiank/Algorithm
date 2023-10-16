##93. 复原 IP 地址
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
# 示例 1：
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s):
        index = 0
        k = 0
        self.n = len(s)
        self.s = s
        self.res = []
        combination = ""
        self.dfs(index, k, combination)
        if len(s) > 12:
            return []
        return self.res

    def dfs(self, index, k, combination):
        if index >= 4 or k >= self.n:
            if index == 4 and len(combination) == self.n + 3:
                self.res.append(combination)
            return
        for i in range(k + 1, min(k + 4, 1 + self.n)):
            if i > k + 1 and self.s[k] == "0":
                continue
            tmp = self.s[k:i]
            if 0 <= int(tmp) and int(tmp) <= 255:
                if index == 0:
                    self.dfs(index + 1, i, combination + tmp)
                else:
                    self.dfs(index + 1, i, combination + "." + tmp)


s = Solution()
print(s.restoreIpAddresses("101023"))

