'''
Created on Sep 12, 2017

@author: qiankunhuang
'''
def bfsShortest(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (vex, path) = queue.pop(0)
        if vex not in visited:
            visited.add(vex)
            for j in graph[vex]:
                if j == end:
                    return path + [j]
                if j not in visited:
                    queue.append((j, path + [j]))
    return False


graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(bfsShortest(graph, 0, 3))


