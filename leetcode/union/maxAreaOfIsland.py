##695. 岛屿的最大面积
# 给你一个大小为 m x n 的二进制矩阵 grid 。
# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
# 岛屿的面积是岛上值为 1 的单元格的数目。
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
# 示例 1：
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
from collections import defaultdict


class union():
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.count = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def add(self, x):
        self.parent[x] = x
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
    def maxAreaOfIsland(self, grid):
        n = len(grid)
        m = len(grid[0])
        u = union(n * m)
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    u.add(i * m + j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for x, y in direction:
                        new_x = x + i
                        new_y = y + j
                        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                            u.union(i * m + j, new_x * m + new_y)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    u.find(i * m + j)
        parents = u.parent
        area_count = defaultdict(int)
        for i in parents:
            if i != -1:
                area_count[i] += 1
        if not area_count.values():
            return 0
        return max(area_count.values())


class Solution:
    def maxAreaOfIsland(self, grid):
        self.direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        self.max_area = 0
        self.visited = [[-1 for i in range(m)] for j in range(n)]
        self.grid = grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and self.visited[i][j] == -1:
                    self.area = 0
                    self.dfs(i, j, n, m)
                    self.max_area = max(self.max_area, self.area)
        return self.max_area

    def dfs(self, x_index, y_index, n, m):
        self.visited[x_index][y_index] = 1
        self.area += 1
        for x, y in self.direction:
            new_x = x_index + x
            new_y = y_index + y
            if 0 <= new_x < n and 0 <= new_y < m and self.grid[new_x][new_y] ==1 and self.visited[new_x][new_y] == -1:
                self.dfs(new_x, new_y, n, m)
