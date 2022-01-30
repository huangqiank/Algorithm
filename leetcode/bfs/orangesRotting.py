##994. 腐烂的橘子
#在给定的网格中，每个单元格可以有以下三个值之一：
#值 0 代表空单元格；
#值 1 代表新鲜橘子；
#值 2 代表腐烂的橘子。
#每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#示例 1：
#输入：[[2,1,1],[1,1,0],[0,1,1]]
#输出：4

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        count = 0
        row = len(grid)
        col = len(grid[0])
        total = 0
        visited = set()
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((i, j))
                    total += 1
                if grid[i][j] == 1:
                    total += 1
        while len(queue) != 0:
            n = len(queue)
            count += 1
            while n > 0:
                n -= 1
                tmp = queue.pop(0)
                for x, y in direction:
                    new_x = tmp[0] + x
                    new_y = tmp[1] + y
                    if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) not in visited and grid[new_x][
                        new_y] == 1:
                        grid[new_x][new_y] = 2
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))

        if len(visited) == total:
            return max(count - 1, 0)
        return -1