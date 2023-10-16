##210. 课程表 II
##现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
##例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

## dfs
class Solution:
    def findOrder(self, numCourses, prerequisites):
        adjacent = {i: [] for i in range(numCourses)}
        self.flag = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            adjacent[i].append(j)
        self.res = []
        for i in range(numCourses):
            if self.dfs(i, adjacent) is False:
                return []
        return self.res

    def dfs(self, index, adjacent):
        if self.flag[index] == 2:
            return False
        if self.flag[index] == 1:
            return True
        self.flag[index] = 2
        for j in adjacent[index]:
            if self.dfs(j, adjacent) is False:
                return False
        self.res.append(index)
        self.flag[index] = 1
        return True


s = Solution()
print(s.findOrder(2, [[1, 0]]))


##bfs
class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree = [0 for i in range(numCourses)]
        res = []
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
            res.append(index)
            numCourses -= 1
            for j in adjacent[index]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        if numCourses != 0:
            return []
        return res