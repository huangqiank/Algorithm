'''
Created on Sep 12, 2017

@author: qiankunhuang
'''
def dfs(graph,start,visit_path= [],visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for vertex in graph[start]:
        if vertex not in visited:
            visit_path.append(vertex)
            dfs(graph, vertex, visit_path, visited)
    return visit_path,visited
graph={0:{1,4},1:{0,3,2},2:{1,3},3:{1,4,2},4:{3,0}}
print dfs(graph,0)


def bfs2(graph,start):
    visited= set()
    path  = []
    queue = [start]
    while queue:
        vec = queue.pop(0)
        if vec not in visited:  
            path.append(vec)
            queue.extend(graph[vec]-visited)
            visited.add(vec)
    return path
def bfs(graph,start):
    visited= set()
    path  = []
    queue = [start]
    while queue:
        vec = queue.pop(0)
        if vec not in visited:
            for j in graph[vec]:
                if j not in visited:
                    path.append(j)
                    queue.append(j)
        visited.add(vec)
    return path,visited
    