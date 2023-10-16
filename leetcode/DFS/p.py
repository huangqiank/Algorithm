##if nums[i] == nums[i-1] and nums[i] = path[-1]:
## continue
import collections


class Solution:
    def subsets(self, nums):
        nums = sorted(nums)
        self.res = []
        index = 0
        path = []
        self.backtrack(index, nums, path)
        return self.res

    ##no nums[i-1]   no nums[i]
    def backtrack(self, index, nums, path):
        if index == len(nums):
            self.res.append(path)
            return
        if index >= 1 and len(path) > 0 and nums[index] == nums[index - 1] and nums[index] != path[-1]:
            self.backtrack(index + 1, nums, path)
        else:
            self.backtrack(index + 1, nums, path + [nums[index]])
            self.backtrack(index + 1, nums, path)

    def backtrack1(self, index, nums, path):
        self.res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.backtrack(i + 1, nums, path + [nums[i]])


s = Solution()
print(s.subsets([1, 2, 3]))


class Solution:
    def permute(self, nums):
        self.res = []
        combination = []
        used = [-1 for i in range(nums)]
        self.dfs(nums, combination, used)
        return self.res

    def dfs(self, nums, combination, used):
        if len(combination) == len(nums):
            self.res.append(combination)
            return
        for i in range(len(nums)):
            if used[i] == -1:
                used[i] = 1
                self.dfs(nums, combination + nums[i], used)
            used[i] = -1


class Solution:
    def permuteUnique(self, nums):
        self.res = []
        path = []
        index = 0
        visited = [-1 for i in range(len(nums))]
        nums = sorted(nums)
        self.dfs(nums, index, path, visited)

    def dfs(self, nums, index, path, visited):
        if index == len(nums):
            self.res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == -1:
                continue
            if visited[i] == -1:
                visited[i] = 1
                self.dfs(nums, index + 1, path + nums[i], visited)
                visited = -1


class Solution:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        index = 0
        self.res = []
        combination = []
        self.dfs(candidates, target, index, n, combination)
        return self.res

    def dfs(self, candidates, target, index, n, combination):
        if index == n or target < 0:
            if target == 0:
                self.res.append(combination)
            return
        for i in range(int(target / candidates[index]) + 1):
            self.dfs(candidates, target - candidates[index] * i, index + 1, n, combination + [candidates[index]] * i)


class Solution:
    def combinationSum2(self, candidates, target):
        self.res = []
        self.num_count = collections.defaultdict(int)
        for num in candidates:
            self.num_count[num] += 1

        self.nums = list(self.num_count.keys())
        n = len(self.nums)
        index = 0
        combination = []
        self.dfs(index, n, target, combination)
        return self.res

    def dfs(self, index, n, target, combination):
        if index == n or target < 0:
            if target == 0:
                self.res.append(combination)
            return
        num = self.nums[index]
        for i in range(min(int(target / num), self.num_count[num]) + 1):
            self.dfs(index + 1, n, target - num * i, combination + [num] * i)


class Solution:
    def partition(self, s):
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j] and (j - i == 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
        self.dp = dp
        index = 0
        self.res = []
        combination = []
        self.dfs(index, n, combination)
        return self.res

    def dfs(self, index, n, combination):
        if index >= n:
            self.res.append(combination)
            return
        for i in range(index, n):
            if self.dp[index][i] == 1:
                self.dfs(i + 1, n, combination + [s[index:i + 1]])


class Solution:
    def restoreIpAddresses(self, s):
        if len(s) > 12 or len(s) < 4:
            return []
        self.res = []
        index = 0
        n = len(s)
        combination = []
        self.dfs(index, n, combination, s)
        return self.res

    def dfs(self, index, n, combiantion, s):
        if index >= n:
            if len(combiantion) == 4:
                self.res.append(".".join(combiantion))
            return
        for i in range(index + 1, min(index + 4, 1 + n), 1):
            if i > index + 1 and s[index] == "0":
                continue
            if int(s[index:i]) >= 0 and int(s[index:i]) <= 255:
                self.dfs(i, n, combiantion + [s[index:i]], s)


class Solution:
    def exist(self, board, word):
        self.direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        index = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[-1 for i in range(len(board[0]))] for j in range(len(board))]
                if self.dfs(i, j, index, visited, word, board):
                    return True
        return False

    def dfs(self, left, right, index, visited, word, board):
        if left >= len(board) or right >= len(board[0]) or left < 0 or right < 0 or visited[left][
            right] == 1 or index == len(word):
            if index == len(word):
                return True
            return False
        if board[left][right] == word[index]:
            visited[left][right] = 1
            for direct in self.direction:
                if self.dfs(left + direct[0], right + direct[1], index + 1, visited, word, board):
                    return True
            visited[left][right] = -1
        return False


print(ord("a"))
print(ord("z"))
print(ord("A"))
print(ord("Z"))
print()

from collections import defaultdict, deque


class Solution345:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        self.graph = self.construct_graph(flights)
        self.min_cost = float("inf")
        cost = 0
        visited = set()
        self.dfs(src, dst, k + 1, cost, visited)
        if self.min_cost == float("inf"):
            return -1
        return int(self.min_cost)

    def construct_graph(self, flights):
        graph = defaultdict(list)
        for i, j, price in flights:
            graph[i].append([j, price])
        return graph

    def dfs(self, src, dft, k, cost, visited):
        if src == dft:
            self.min_cost = min(self.min_cost, cost)
            return
        if k <= 0 or cost >= self.min_cost:
            return
        for next, price in self.graph[src]:
            if next not in visited:
                visited.add(next)
                self.dfs(next, dft, k - 1, cost + price, visited)
                visited.remove(next)


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
s = Solution345()
print(s.findCheapestPrice(n, flights, 0, 3, 1))


class Solution:
    def longestIncreasingPath(self, matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.ans = 0
        self.matrix = matrix

        for i in range(self.n):
            for j in range(self.m):
                visited = set()
                path = []
                self.dfs(i, j, visited, path)
        return self.ans

    def dfs(self, left, right, visited, path):
        self.ans = max(self.ans, len(path))
        tmp = self.matrix[left][right]
        for i in [1, -1]:
            for j in [1, -1]:
                new_i = left + i
                new_j = right + j
                if new_i < 0 or new_i >= self.n or new_j < 0 or new_j >= self.m or (new_i, new_j) in visited:
                    continue
                if self.matrix[new_i][new_j] > tmp:
                    visited.add((new_i, new_j))
                    self.dfs(new_i, new_j, visited, path + [self.matrix[new_i][new_j]])
                    visited.pop()




