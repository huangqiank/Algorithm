##Given n nodes labeled from 0 to n-1 and a list of undirected edges
##(each edge is a pair of nodes),
##write a function to check whether these edges make up a valid tree.
##Example 1:
##Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
##Output: true
##Example 2:
##Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
##Output: false
##Note: you can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
##判断全联通
##判断有无环和第三条一样
##判断树状结构 m =n-  1
class Solution:
    def validTree(self, n, edges):
        m = len(edges)
        if n - 1 != m:
            return False
        graph = {}
        visited = set()
        for x, y in edges:
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x].append(y)
            if y not in graph:
                graph[y] = [x]
            else:
                graph[y].append(x)
        node = edges[0][0]
        self.dfs(visited, node, graph)
        return len(visited) == n

    def dfs(self, visited, node, graph):
        visited[node] = True
        if node not in visited:
            for i in graph[node]:
                self.dfs(visited, i, graph)

    def validTree2(self, n, edges):
        m = len(edges)
        if n - 1 != m:
            return False
        graph = {}
        visited = set()
        for x, y in edges:
            if x not in graph:
                graph[x] = [y]
            else:
                graph[x].append(y)
            if y not in graph:
                graph[y] = [x]
            else:
                graph[y].append(x)
        node = edges[0][0]
        self.bfs(visited, node, graph)
        return len(visited) == n

    def bfs(self, visited, node, graph):
        queue = [node]
        while queue:
            node = queue.pop()
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node])
