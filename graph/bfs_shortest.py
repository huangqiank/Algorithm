'''
Created on Sep 12, 2017

@author: qiankunhuang
'''
def bfs_shortest(graph , start_vertex , end_vertex):
    queue = [(start_vertex,[start_vertex])]
    visited = set()
    while queue:
        (vertex,path) = queue.pop(0)
        if vertex not in visited:
            for next in graph[vertex] :
                if next not in visited:
                    if next == end_vertex:
                        return path + [next]
                queue.append((next,path+[next]))
            visited.add(vertex)
    return None
graph={0:{1,4},1:{0,3,2},2:{1,3},3:{1,4,2},4:{3,0}}
print bfs_shortest(graph,0,2)   


