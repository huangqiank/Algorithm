##There are a total of n courses you have to take, labeled from 0 to n-1.
##Some courses may have prerequisites, for example
# to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
##Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all_class courses?
##Example 1:
##Input: 2, [[1,0]]
##Output: true
##Explanation: There are a total of 2 courses to take.
##             To take course 1 you should have finished course 0. So it is possible.
##Example 2:

##Input: 2, [[1,0],[0,1]]
##Output: false
##Explanation: There are a total of 2 courses to take.
##             To take course 1 you should have finished course 0, and to take course 0 you should
##             also have finished course 1. So it is impossible.
##Note:
##The input prerequisites is a graph represented by a list of edges,
# not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
## 判断有没有环
##在每一次的循环中寻找是否有环，这是有向的

class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjacent = [[] for i in range(numCourses)]
        flag = [0 for i in range(numCourses)]
        for x, y in prerequisites:
            adjacent[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i, adjacent, flag):
                return False
        return True

    def dfs(self, i, adjacent, flag):
        if flag[i] == -1:
            return True
        if flag[i] == 1:
            return False
        flag[i] = 1
        for j in adjacent[i]:
            if not self.dfs(j, adjacent, flag):
                return False
        flag[i] = -1
        return True


numCourses = 3
prerequisites = [[1, 0], [2, 1]]
s = Solution()
print(s.canFinish(numCourses, prerequisites))
