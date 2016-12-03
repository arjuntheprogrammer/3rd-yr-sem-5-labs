graph = {
		 'S': ['A', 'B'],
       	 'A': ['C'],
       	 'B': ['C', 'D'],
       	 'C': ['E', 'D'],
       	 'D': ['F'],
       	 'E': ['G'],
         'F': ['G']
         
        }

def dfs(graph, start, end, a, visited=None):
	#print (start)
	if visited is None:
		visited = [start]

	# if(len(a)==n):
	# 	return 
	if(start==end):
		a.append(end)
		return 1  

	a.append(start) 
        
	for next in graph[start]:
		if next not in visited:
			visited.append(next)  
			if(dfs(graph, next,end, a, visited)==1):
				return 1;


def ids(graph, start, end):
	level=-1
	while(True):
		level+=1
		a=[]
		ii=0
		if(ids1(graph, start, end,level,a, ii) ==1):
			print(a)
			break;
		else:
			print a	


def ids1(graph, start, end, level, a, ii=0, visited=None):
	#print (start)
	#print ii
	if visited is None:
		visited = [start]


	# if(len(a)==n):
	# 	return 
	if(start==end):
		a.append(end)
		return 1  

	a.append(start) 
    
	if(level==ii):
		return 2
	

	for next in graph[start]:
		if next not in visited:
			visited.append(next)  
			if(ids1(graph, next,end,level,  a, ii+1, visited)==1):
				return 1;
			else:
				continue;	





if __name__ == '__main__':
	a=[]
	start='S'
	end='G'

	print("out put for dfs=")
	dfs(graph,start, end , a )	
	print (a)


	print("\n\noutput for iterative deepning")
	ids(graph, start, end) 

