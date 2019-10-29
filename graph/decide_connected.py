'''
Created on Sep 18, 2017

@author: qiankunhuang
'''


def Connected(graph, start):
    visited = set()
    queue= [start]
    while queue:
        vex = queue.pop(0)
        if vex not in visited:
            visited.add(vex)
            queue.extend(graph[vex] - visited)
    return len(graph) == len(visited)


def reverse(graph):
    new = {}
    for i in graph:
        for j in graph[i]:
            if j not in new:
                graph[j] = {i}
            else:
                graph[j].add(i)
    return new

graph = {0: {2}, 1: {3}, 2: {0}, 3: {0}, 4: {0}}
print(Connected(graph, 0))