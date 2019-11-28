##Given a 2d grid map of '1's (land) and '0's (water),
# count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3


class Solution:
    def numIslands(self, grid):
        self.direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        if not grid:
            return 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        count = 0
        market = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if not market[i][j] and grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, market, grid, m, n)
        return count

    def dfs(self, i, j, market, grid, m, n):
        if not market[i][j]:
            market[i][j] = True
            for k in self.direction:
                row = i + k[0]
                col = j + k[1]
                if 0 <= row < m and 0 <= col < n and not market[row][col] and grid[row][col] == "1":
                    self.dfs(row, col, market, grid, m, n)

