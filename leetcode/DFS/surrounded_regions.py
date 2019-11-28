##Given a 2D board containing 'X' and 'O' (the letter O),
##capture all regions surrounded by 'X'.
##A region is captured by flipping all 'O's into 'X's in that surrounded region.
##Example:
##X X X X
##X O O X
##X X O X
##X O X X
##After running your function, the board should be:
##X X X X
##X X X X
##X X X X
##X O X X
##Explanation:
##Surrounded regions shouldn’t be on the border,
##which means that any 'O' on the border of the board are not flipped to 'X'.
##Any 'O' that is not on the border and it is not connected to an 'O' on the border
##will be flipped to 'X'. Two cells are connected
##if they are adjacent cells connected horizontally or vertically.
class Solution:
    def solve(self, board):
        self.direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        visited = set()
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    if board[i][j] == "O":
                        self.dfs(i, j, board, visited, n, m)
        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
        return board

    def dfs(self, i, j, board, visited, n, m):
        if i >= n or j >= m or i < 0 or j < 0 or board[i][j] != "O":
            return
        if (i,j) in visited:
            return
        board[i][j] = "#"
        for direction in self.direction:
            new_i = i + direction[0]
            new_j = j + direction[1]
            self.dfs(new_i, new_j, board, visited, n, m)
        visited.add((i,j))


board =[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s = Solution()
print(s.solve(board))
