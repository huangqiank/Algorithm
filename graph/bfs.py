'''
Created on Sep 12, 2017

@author: qiankunhuang
'''
def bfs(graph,start):
    visited , queue = set() , [start]
    visit_path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:   
            visited.add(vertex)
            visit_path.append(vertex)
            queue.extend(graph[vertex])
    return visit_path
def bfs2(graph,start):
    visited , queue = set() , [start]
    visit_path = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:   
            visited.add(vertex)
            for j in graph[vertex]:
                if j not in visited:
                    visit_path.append(j)
                    queue.append(j)
    return visit_path
graph={0:{1,4},1:{0,3,2},2:{1,3},3:{1,4,2},4:{3,0}}
print bfs(graph,0)
graph={0:{1,4},1:{0,3,2},2:{1,3},3:{1,4,2},4:{3,0}}
print bfs(graph,0)