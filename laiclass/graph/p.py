'''
Created on Dec 20, 2017

@author: qiankunhuang
'''
def dfs(graph,node):
    visited=set()
    path  = [node]
    help(graph,node,visited,path)
    return path
    
def help(graph,node,visited,path):
    visited.add(node)
    for i in graph[node]:
        if i not in visited:
            help(graph,i,visited,path+[i])
    return 
graph={0:{1,4},1:{0,3,2},2:{1,3},3:{1,4,2},4:{3,0}}


a= [[False for i in range(3)] for j in range(5)]
print(a)
