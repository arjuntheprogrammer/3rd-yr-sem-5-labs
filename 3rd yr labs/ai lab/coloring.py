#graph=[[0 for x in xrange(4)] for y in xrange(4)]
###################################################
graph=[]

graph.append([])
graph.append([])
graph.append([])
graph.append([])


graph[0].append(0)
graph[0].append(1)
graph[0].append(1)
graph[0].append(1)


graph[1].append(1)
graph[1].append(0)
graph[1].append(1)
graph[1].append(0)


graph[2].append(1)
graph[2].append(1)
graph[2].append(0)
graph[2].append(1)

graph[3].append(1)
graph[3].append(0)
graph[3].append(1)
graph[3].append(0)

V=4 #no. of vertices
################################
def print_sol(color):
	for  i in xrange(V):
		print("node=", i, " color=", color[i])
#################################
def isSafe(v, graph, color, c):
	for i in xrange(V):
		if( graph[v][i]!=0 and c==color[i]):
			return False

	return True		

##################################
def graph_util(graph, m, color, v):
	if(v==V):
		return True

	for c in xrange(1, m+1):
		if (isSafe(v, graph, color, c)):
			color[v]=c;
			if(graph_util(graph, m, color, v+1)==True):
				return True

			color[v]=0;	

	return False		

##################################	
def graphColor(graph, m , color):
	for i in xrange(V):
		color.append(0);

	return graph_util(graph, m, color, 0)		

			
######################################

if __name__ == '__main__':
	color=[]
	for m in xrange(1, V+1):
		if(graphColor(graph,m, color)==True):
			print ("graph can be colored in "+`m`+" colors..")
			print_sol(color)
			break
