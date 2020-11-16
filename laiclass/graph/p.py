'''
Created on Dec 20, 2017

@author: qiankunhuang
'''


def dfs(graph, node):
    visited = set()
    path = [node]
    help(graph, node, visited, path)
    return path


def help(graph, node, visited, path):
    visited.add(node)
    for i in graph[node]:
        if i not in visited:
            help(graph, i, visited, path + [i])
    return


graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}

a = [[False for i in range(3)] for j in range(5)]
print(a)


def bfs(graph, start):
    queue = [start]
    visited = set()
    visited_path = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited_path.append(node)
            visited.add(node)
            queue.extend(graph[node])
    return


def dfs(graph, start, visited=None, visited_path=[]):
    if visited is None:
        visited = set()
    visited.add(start)
    for i in graph[start]:
        if i not in visited:
            visited_path.append(i)
            dfs(graph, i, visited, visited_path)
    return visited_path


def reverse(graph):
    new = {}
    for i in graph.keys():
        for j in graph[i]:
            if j not in new:
                new[j] = [i]
            else:
                new[j].append(i)
    return new


def connected(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return visited


def less_than_k(graph, start, end, k):
    visited = set()
    queue = [start]
    while queue and k >= 0:
        n = len(queue)
        while n > 0:
            node = queue.pop(0)
            visited.add(node)
            if node == end:
                return True
            ## queue.append(graph[node] - visited)
            for i in graph[node]:
                if i not in visited:
                    queue.append(i)
            n -= 1
        k -= 1
    return False
