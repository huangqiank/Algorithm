##79. 单词搜索
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
# 如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true


class Solution:
    def exist(self, board, word):
        self.word = word
        self.board = board
        begins = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    begins.append((i, j))
        if len(begins) == 0:
            return False
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for (x_index, y_index) in begins:
            index = 0
            visited = set()
            if self.dfs(x_index, y_index, index, visited):
                return True
        return False

    def dfs(self, x_index, y_index, index, visited):
        if self.board[x_index][y_index] != self.word[index]:
            return False
        if index == len(self.word) - 1:
            return True
        if self.board[x_index][y_index] == self.word[index]:
            visited.add((x_index, y_index))
            for direction in self.directions:
                new_x = direction[0] + x_index
                new_y = direction[1] + y_index
                if new_x < 0 or new_x >= len(self.board) or new_y < 0 or new_y >= len(self.board[0]) or (
                        new_x, new_y) in visited:
                    continue
                if self.dfs(new_x, new_y, index + 1, visited):
                    return True
            visited.remove((x_index, y_index))
        return False

    def dfs1(self, x_index, y_index, index, visited):
        if x_index < 0 or x_index >= len(self.board) or y_index < 0 or y_index >= len(self.board[0]) or (
                x_index, y_index) in visited:
            return False
        if self.board[x_index][y_index] == self.word[index] and index == len(self.word) - 1:
            return True
        if self.board[x_index][y_index] == self.word[index]:
            visited.add((x_index, y_index))
            for i in [-1, 1]:
                if self.dfs(x_index + i, y_index, index + 1, visited):
                    return True
                if self.dfs(x_index - i, y_index, index + 1, visited):
                    return True
                if self.dfs(x_index, y_index + i, index + 1, visited):
                    return True
                if self.dfs(x_index, y_index - i, index + 1, visited):
                    return True
            visited.remove((x_index, y_index))
        return False


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"



board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"



board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"


board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"

s1 = Solution()
board = [["a", "b"], ["c", "d"]]
word = "cdba"
s1.exist(board, word)
##ab
##cd

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
s.exist(board, word)


## abce
## sfes
## adee
## abceseeefs


class Solution:
    def exist(self, board, word):
        self.direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    index = 1
                    if self.dfs(board, word, i, j, n, m, index, visited):
                        return True
        return False

    def dfs(self, board, word, i, j, n, m, index, visited):
        if index == len(word):
            return True
        for x, y in self.direction:
            new_x = x + i
            new_y = y + j

            if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in visited and board[new_x][new_y] == word[
                index]:
                visited.add((new_x, new_y))
                if self.dfs(board, word, new_x, new_y, n, m, index + 1, visited):
                    return True
                visited.remove((new_x, new_y))
        return False


class Solution131:
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])
        self.direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.board = board
        for i in range(n):
            for j in range(m):
                self.visited = set()
                if board[i][j] == word[0]:
                    self.visited = set()
                    self.visited.add((i,j))
                    if self.dfs(i, j, n, m, 1, word):
                        return True
        return False

    def dfs(self, i, j, n, m, index, word):
        if index == len(word):
            return True
        self.visited.add((i, j))
        for x, y in self.direction:
            new_x = i + x
            new_y = j + y
            if 0 <= new_x < n and 0 <= new_y <m and (new_x, new_y) not in self.visited and word[index] == self.board[new_x][new_y]:
                if self.dfs(new_x, new_y, n, m, index + 1, word):
                        return True
        self.visited.remove((i, j))
        return False


s = Solution131()
a = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
b = "ABCCED"












class Solution134:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.diriection = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(1):
            for j in range(1):
                if board[i][j] == word[0]:
                    self.visit = set()
                    if self.dfs(i,j,0,word,n,m,board,0):
                        return True
        return False
    def dfs(self,x,y,index,word,n,m,board,step):
        print(x, y, board[x][y], step )
        if index == len(word)-1:
            return True
        self.visit.add((x,y))
        for i,j in self.diriection:
            new_x = x + i
            new_y = y + j
            if (new_x,new_y) not in self.visit and 0<= new_x< m and 0<= new_y< n and board[new_x][new_y] == word[index+1]:
                if self.dfs(new_x, new_y, index+1, word, n, m, board,step+1):
                    return True
        self.visit.remove((x,y))
        return False
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word ="ABCESEEEFS"
s = Solution134()
print(s.exist(board,word))
## a b c e
## s f e s
## a s e e
s