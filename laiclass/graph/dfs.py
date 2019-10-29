'''
Created on Sep 12, 2017

@author: qiankunhuang
'''



def dfs(graph, start, visitPath=[], visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for vertex in graph[start]:
        if vertex not in visited:
            visitPath.append(vertex)
            dfs(graph, vertex, visitPath, visited)
    return visitPath, visited


graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(dfs(graph, 0))


def bfs(graph, start):
    visited = set()
    visitedPath = []
    queue = [start]
    while queue:
        vex = queue.pop(0)
        if vex not in visited:
            visited.add(vex)
            for i in graph(vex):
                if i not in visited:
                    visitedPath.append(i)
                    queue.append(i)
    return visited, visitedPath

def bfs3(graph, start):
    path = []
    visited = set()
    queue = [start]
    while queue:
        vex = queue.pop(0)
        if vex not in visited:
            visited.add(vex)
            path.append(vex)
            for j in graph[vex]:
                if j not in visited:
                    queue.append(j)
    return path


def dfs3(graph, start, path=[], visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        visited.add(start)
        for j in graph[start]:
            if j not in visited:
                path.append(j)
                dfs(graph,j,path,visited)
    return path


graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(bfs3(graph, 0))
print(dfs3(graph, 0))
