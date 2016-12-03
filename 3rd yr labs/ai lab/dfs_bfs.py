graph = {'A': ['B', 'C'],
           	 'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}

"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

"""
n=len(graph)

"""
def dfs(graph, start,a, visited=None):
    if visited is None:
        visited = set()
    
    if(len(a)==n):
    	return 

    visited.add(start)
    a+=start
   
    for next in graph[start] - visited:
        dfs(graph, next,a, visited)
    return visited
"""

def dfs1(graph, start,a, visited=None):
	if visited is None:
		visited = [start]
	if(len(a)==n):
		return 
	a+=start 
        
	for next in graph[start]:
		if next not in visited:
			visited+=next  
			dfs1(graph, next,a, visited)    		

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

#bfs(graph, 'A')

def bfs1(graph, start):
	queue=[start]
	visited=[]
	while queue:
		vertex=queue.pop(0)
		if vertex not in visited:
			visited+=vertex
			for i in graph[vertex]:
				queue+=i
	return visited


a=[]

dfs1(graph, 'C',a) # {'E', 'D', 'F', 'A', 'C', 'B'}             
print (a)

print (bfs1(graph, 'C'))


