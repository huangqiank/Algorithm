##261. 以图判树
# 给定编号从 0 到 n - 1 的 n 个结点。
# 给定一个整数 n 和一个 edges 列表，
# 其中 edges[i] = [ai, bi] 表示图中节点 ai 和 bi 之间存在一条无向边。
# 如果这些边能够形成一个合法有效的树结构，则返回 true ，否则返回 false 。
# 示例 1：
# 输入: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# 输出: true


##
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ##1. 没有环
        ##2. 全联通
        ## n- 1 = len(edges)
        ## 全联通
        if n - 1 != len(edges):
            return False
        if n == 1:
            return True
        visited = set()
        queue = [0]
        graph = {}
        for i, j in edges:
            graph[i] = graph.get(i, []) + [j]
            graph[j] = graph.get(j, []) + [i]
        if len(graph.keys()) != n:
            return False
        while queue:
            m = len(queue)
            while m> 0 :
                node = queue.pop(0)
                m -= 1
                if node in visited:
                    continue
                visited.add(node)
                for i in graph[node]:
                    queue.append(i)
        if len(visited) !=  n:
            return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        if n == 1:
            return True
        self.visited = set()
        graph = {}
        for i, j in edges:
            graph[i] = graph.get(i, []) + [j]
            graph[j] = graph.get(j, []) + [i]
        if len(graph.keys()) != n:
            return False
        self.dfs(0,graph)
        return len(self.visited) == n

    def dfs(self, node, graph):
        if node in self.visited:
            return
        self.visited.add(node)
        for i in graph[node]:
            self.dfs(i, graph)
