##305. 岛屿数量 II
# 给你一个大小为 m x n 的二进制网格 grid 。网格表示一个地图，其中，0 表示水，1 表示陆地。最初，grid 中的所有单元格都是水单元格（即，所有单元格都是 0）。
# 可以通过执行 addLand 操作，将某个位置的水转换成陆地。给你一个数组 positions ，其中 positions[i] = [ri, ci] 是要执行第 i 次操作的位置 (ri, ci) 。
# 返回一个整数数组 answer ，其中 answer[i] 是将单元格 (ri, ci) 转换为陆地后，地图中岛屿的数量。
# 岛屿 的定义是被「水」包围的「陆地」，通过水平方向或者垂直方向上相邻的陆地连接而成。你可以假设地图网格的四边均被无边无际的「水」所包围。
# 示例 1：
# 输入：m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# 输出：[1,1,2,3]
# 解释：
# 起初，二维网格 grid 被全部注入「水」。（0 代表「水」，1 代表「陆地」）
# - 操作 #1：addLand(0, 0) 将 grid[0][0] 的水变为陆地。此时存在 1 个岛屿。
# - 操作 #2：addLand(0, 1) 将 grid[0][1] 的水变为陆地。此时存在 1 个岛屿。
# - 操作 #3：addLand(1, 2) 将 grid[1][2] 的水变为陆地。此时存在 2 个岛屿。
# - 操作 #4：addLand(2, 1) 将 grid[2][1] 的水变为陆地。此时存在 3 个岛屿。


class union:
    def __init__(self, index):
        self.count = 0
        self.parent = [0 for i in range(index)]
        self.rank = [0 for i in range(index)]

    def find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def add(self, index):
        self.parent[index] = index
        self.count += 1

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
            self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions):
        res = []
        u = union(m * n)
        stone_set = set()
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for x, y in positions:
            index = x * n + y
            if index in stone_set:
                res.append(u.count)
            else:
                stone_set.add(index)
                u.add(index)
                for direct in direction:
                    new_x = x + direct[0]
                    new_y = y + direct[1]
                    new_index = new_x * n + new_y
                    if 0 <= new_x < m and 0 <= new_y < n:
                        if new_index in stone_set:
                            u.union(index, new_index)
                res.append(u.count)
        return res


class UnionFind:
    def __init__(self, n: int):
        self.root = list(range(n))
        self.size = [1] * n
        self.islandCnt = 0  # 当前岛屿数量

    def findroot(self, x: int) -> int:
        while self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def unite(self, x: int, y: int) -> bool:
        root1, root2 = self.findroot(x), self.findroot(y)
        if root1 == root2:
            return False
        if self.size[root1] >= self.size[root1]:
            bigRoot, smallRoot = root1, root2
        else:
            bigRoot, smallRoot = root2, root1
        self.root[smallRoot] = bigRoot
        self.size[bigRoot] += self.size[smallRoot]
        self.islandCnt -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.findroot(x) == self.findroot(y)


class Solution4:
    def numIslands2(self, m: int, n: int, positions):

        def calcID(x, y):
            return x * n + y

        def inMap(x, y):
            return 0 <= x < m and 0 <= y < n

        uf = UnionFind(m * n)
        islandSet = set()
        ans = []
        DIREC = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in positions:
            loc = calcID(x, y)
            if loc in islandSet:  # 如果是重复的点，跳过
                ans.append(uf.islandCnt)
            else:
                islandSet.add(loc)  # 先当成单独的岛屿，之后检查四周的点
                uf.islandCnt += 1
                for dx, dy in DIREC:
                    nx, ny = x + dx, y + dy
                    if inMap(nx, ny):
                        nloc = calcID(nx, ny)
                        if nloc in islandSet:
                            uf.unite(loc, nloc)

                ans.append(uf.islandCnt)
        return ans


m = 3
n = 3
positions = [[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]]

##[1,2,3,4,3,2,1]
s = Solution()
print(s.numIslands2(m, n, positions))
s = Solution4()
print(s.numIslands2(m, n, positions))
# 0 1 1
# 1 0 1
# 0 1 0




