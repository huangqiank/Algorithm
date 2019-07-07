'''
Created on Sep 18, 2017

@author: qiankunhuang
'''
def decide_connected(graph , start):
    queue = [start]
    path = []
    visited = set()
    while queue:
        vec = queue.pop(0)
        if vec not in visited:
            visited.add(vec)
            path.append(vec)
            queue.extend(graph[vec] - visited)
    return len(graph) == len(visited)   
def reverse(graph):
    new_graph={}
    for i in graph:
        for j in graph[i]:
            if j not in new_graph:
                new_graph[j] = {i}
            else:
                new_graph[j].add(i)
    return new_graph

                

def connected(graph , start):
    if decide_connected(graph , start) and  decide_connected(reverse(graph), start):
        return True
    return False  
graph={0:{2},1:{3},2:{0},3:{0},4:{0}}
print (connected(graph , 0)) 
