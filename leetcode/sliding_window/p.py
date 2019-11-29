class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        adajacent = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        for x, y in prerequisites:
            adajacent[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i, adajacent, visited):
                return False
        return True

    def dfs(self, node, adajacent, visited):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        for i in adajacent[node]:
            if not self.dfs(i, adajacent, visited):
                return False
        visited[node] = 1
        return True
