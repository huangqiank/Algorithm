'''
Created on Sep 26, 2017

@author: qiankunhuang
'''


def dfs(graph,start):
    path=[start]
    visited = set()
    dfs_help(graph,start,path,visited)
    return path
    
def dfs_help(graph,start,path,visited):
    visited.add(start)
    for j in graph[start]:
        if j not in visited:
            path.append(j)
            dfs_help(graph , j ,path , visited )
    return path
        
graph={0:{1,4},1:{0,3,2,4},2:{1,3,4},3:{1,4,2,4},4:{3,0}}
print (dfs(graph,0)  )