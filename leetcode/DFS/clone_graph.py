##Given a reference of a node in a connected undirected graph,
# return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
# Example:
# Input:
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},
# {"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":
# [{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node):
        look = {}

        def dfs(node):
            if not node:
                return
            if node in look:
                return look[node]
            new = Node(node.val, [])
            look[node] = new
            for i in node.neighbors:
                new.neighbors.append(dfs(i))
            return new

        return dfs(node)

    def cloneGraph2(self, node):
        look = {}
        def bfs(node):
            if not node:
                return
            clone = Node(node.val, [])
            look[node] = clone
            queue = [node]
            while queue:
                tmp = queue.pop(0)
                for i in tmp.neighbors:
                    if i not in look:
                        look[i] = Node(i.val, [])
                        queue.append(i)
                    look[tmp].neighbors.append(look[i])
            return clone

        return bfs(node)
