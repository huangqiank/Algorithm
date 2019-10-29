'''
Created on Sep 12, 2017

@author: qiankunhuang
'''


###bfs 广度优先，添加自己这一层的数值，下一层的放入queue，逐步去除

def bfs(graph, start):
    visited, queue = set(), [start]
    visited_path = []
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            visited_path.append(vertex)
            queue.extend(graph[vertex])
    return visited_path


def bfs2(graph,start):
    visited = set()
    queue= [start]
    visited_path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            visited_path.append(vertex)
            for j in graph[vertex]:
                if j not in visited:
                    queue.append(j)
    return visited_path



graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(bfs(graph, 0))
graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(bfs(graph, 0))

