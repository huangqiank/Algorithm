'''
Created on Sep 12, 2017

@author: qiankunhuang
'''


def lessthank(graph, start, end, k):
    queue1 = [start]
    queue2 = []
    visited = set()
    while (queue1 and queue2) and k >= 0:
        while queue1 and k >= 0:
            vertex = queue1.pop(0)
            if vertex not in visited:
                if vertex == end:
                    return True
                for next in graph[vertex] - visited:
                    queue2.append(next)
                visited.add(vertex)
                k = k - 1
        while queue2 and k >= 0:
            vertex = queue2.pop(0)
            if vertex not in visited:
                if vertex == end:
                    return True
                for next in graph[vertex] - visited:
                    queue1.append(next)
                visited.add(vertex)
                k = k - 1
        return False


def lessthank2(graph, start, end, k):
    queue = [start]
    visited = set()
    while queue and k >= 0:
        n = len(queue)
        while n > 0:
            n -= 1
            vertex = queue.pop(0)
            if vertex not in visited:
                if vertex == end:
                    return True
                for next in graph[vertex] - visited:
                    queue.append(next)
                visited.add(vertex)
        k -= 1
    return False

def lessThanK(graph, start, end, k):
    queue = [start]
    visited = set()
    while queue and k >= 0:
        n = len(queue)
        k -= 1
        while n > 0:
            n-=1
            vex = queue.pop(0)
            if vex not in visited:
                if vex == end:
                    return True
                visited.add(vex)
                for i in graph[vex]:
                    if i not in visited:
                        queue.append(i)
    return False


graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(lessThanK(graph, 1, 4, 1))

graph = {0: {1, 4}, 1: {0, 3, 2}, 2: {1, 3}, 3: {1, 4, 2}, 4: {3, 0}}
print(lessthank2(graph, 1, 4, 2))
