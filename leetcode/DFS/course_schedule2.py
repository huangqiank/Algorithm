##There are a total of n courses you have to take,
##labeled from 0 to n-1.
##Some courses may have prerequisites,
# for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
##Given the total number of courses and a list of prerequisite pairs,
##return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.
##Example 1:
##Input: 2, [[1,0]]
##Output: [0,1]
##Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
##             course 0. So the correct course order is [0,1] .
##Example 2:

##Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
##Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        visited_path = []
        flag = [0 for i in range(numCourses)]
        adjacent = [[] for i in range(numCourses)]
        for x,y in prerequisites:
            adjacent[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i, visited_path, flag, adjacent):
                return []
        return visited_path

    def dfs(self, i, visited_path, flag, adjacent):
        if flag[i] == 1:
            return True
        if flag[i] == -1:
            return False
        flag[i] = -1
        for j in adjacent[i]:
            if not self.dfs(j, visited_path, flag, adjacent):
                return False
        ##走完所有子节点才可以添加母节点
        visited_path.append(i)
        flag[i] = 1
        return True
numCourses = 2
prerequisites =[[0,1]]
s =Solution()
print(s.findOrder(numCourses,prerequisites))