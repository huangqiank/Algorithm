'''
Created on Sep 12, 2017

@author: qiankunhuang
'''

graph={0:{1,4},1:{0,3,2},2:{1,3},3:{1,4,2},4:{3,0}}

def graph_edges(graph):
    edges = []
    for i in graph:
        for neighbour in graph[i]:
            edges.append((i, neighbour))
    return edges


print graph_edges(graph)    



def getvec(graph):
    return graph.keys()
print getvec(graph) 
   
  
  
def add_vec(graph , vec):
    if vec not in graph:
        graph[vec]= set()

def add_edge(graph , v1 , v2):  ### have direction
    if v1 not in graph:
        graph[v1]= set()
        graph[v1].add(v2)
    else:
        if v2 not in graph[v1]:
            graph[v1].add(v2)
            
def add_edge2(graph, edge):   ##edge is tulple 
    (v1 , v2) = edge
    add_vec(graph,v1,v2)
    add_vec(graph,v2,v1)

def del_node(graph, node):
    if node in graph:
        del graph[node]
    for i in graph:
        if node in  graph[i]:
            graph[i].remove(node)

def del_edg(graph, v1,v2):
    if v1 in graph:
        graph[v1].discard(v2)
    if v2 in graph:
        graph[v2].discard(v1)

def del_node2(graph,v1):
    if  v1 in graph:
        del graph[v1]
    for j in graph:
            graph[j].discard([v1])
            

                      

   
            
        
        
            
    
       