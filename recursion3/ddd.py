'''
Created on Sep 28, 2017

@author: qiankunhuang
'''
def dfs(graph, start_vertex, visited_path):
    if visited_path is None:
        visited_path = []
    for vertex in graph[start_vertex]:
        if vertex not in visited_path:
            visited_path.append(vertex)
            dfs(graph, vertex, visited_path)
    return visited_path
graph={1:{2,3},2:{4,5},3:{6,7},4:{},5:{},6:{},7:{}}
print dfs(graph,1, [])