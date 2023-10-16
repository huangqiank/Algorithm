##721. 账户合并
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。
# 示例 1：
# 输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts):
        self.email_name = {}
        self.email_index = {}
        self.index_email = {}
        self.email_cnt = 0
        for element in accounts:
            name = element[0]
            for i in range(1, len(element)):
                self.email_name[element[i]] = name
                if element[i] not in self.email_index.keys():
                    self.index_email[self.email_cnt] = element[i]
                    self.email_index[element[i]] = self.email_cnt
                    self.email_cnt += 1
        u = union(self.email_cnt)
        for element in accounts:
            x_index = self.email_index[element[1]]
            for i in range(2, len(element)):
                y_index = self.email_index[element[i]]
                u.union(x_index, y_index)
        tmp = defaultdict(list)
        for i in range(self.email_cnt):
            tmp[u.find(i)].append(i)
        res = []
        for i in tmp.keys():
            account = []
            name = self.email_name[self.index_email[i]]
            account.append(name)
            emails = []
            for j in tmp[i]:
                email = self.index_email[j]
                emails.append(email)
            account += sorted(emails)
            res.append(account)
        return res


class union():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1


accounts = [["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]]

s = Solution()
print(s.accountsMerge(accounts))
