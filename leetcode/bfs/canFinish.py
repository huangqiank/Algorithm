##207. 课程表
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。


class Solution:

    def canFinish(self, numCourses, prerequisites):
        visited = [-1 for i in range(numCourses)]
        adjacent = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            adjacent[i].append(j)
        for i in range(numCourses):
            if self.dfs(i, visited, adjacent) is False:
                return False
        return True

    def dfs(self, course, visited, adjacent):
        if visited[course] == 1:
            return True
        if visited[course] == 0:
            return False
        visited[course] = 0
        for i in adjacent[course]:
            if self.dfs(i, visited, adjacent) is False:
                return False
        visited[course] = 1
        return True


## dfs
class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.flag = [-1 for i in range(numCourses)]
        graph = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            graph[i].append(j)
        for i in range(numCourses):
            if self.dfs(i, graph) is False:
                return False
        return True

    def dfs(self, index, graph):
        if self.flag[index] == 0:
            return False
        if self.flag[index] == 1:
            return True
        self.flag[index] = 0
        for i in graph[index]:
            if self.dfs(i, graph) is False:
                return False
        self.flag[index] = 1
        return True


## 1，2 ->3

## 1-->2 ->3 -->2
##[1,2], [2,3],[3,2]

##bfs

class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0 for i in range(numCourses)]
        adjacent = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            indegree[i] += 1
            adjacent[j].append(i)
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            index = queue.pop(0)
            numCourses -= 1
            for j in adjacent[index]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        if numCourses == 0:
            return True
        return False
