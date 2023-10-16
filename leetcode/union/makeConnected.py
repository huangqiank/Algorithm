##1319. 连通网络的操作次数
# 用以太网线缆将 n 台计算机连接成一个网络，计算机的编号从 0 到 n-1。线缆用 connections 表示，其中 connections[i] = [a, b] 连接了计算机 a 和 b。
# 网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。
# 给你这个计算机网络的初始布线 connections，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请
# 你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。
# 示例 1：
# 输入：n = 4, connections = [[0,1],[0,2],[1,2]]
# 输出：1
# 解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。
# 示例 2：
# 输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# 输出：2


class union:
    def __init__(self, n):
        self.parents = [-1 for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.count = 0
        self.remain = 0

    def add(self, index):
        self.parents[index] = index
        self.count += 1

    def find(self, index):
        if index != self.parents[index]:
            self.parents[index] = self.find(self.parents[index])
        return self.parents[index]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.count -= 1
            self.parents[rootx] = rooty
        else:
            self.remain += 1
class Solution:
    def makeConnected(self, n: int, connections):
        u = union(n)
        for i in range(n):
            u.add(i)
        for i, j in connections:
            u.union(i, j)
        if u.count - 1 <= u.remain:
            return u.count - 1
        return -1


n = 5
connections = [[0, 1], [0, 2], [1, 2]]
s = Solution()
print(s.makeConnected(n, connections))


class Solution:
    def makeConnected(self, n: int, connections):
        if len(connections) < n - 1:
            return -1

        edges = collections.defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)

        seen = set()

        def dfs(u: int):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)

        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1

