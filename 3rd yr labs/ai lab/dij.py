import sys

graph={
	'A': {'C':10, 'D':20},
	'C': {'A':10, 'B':20, 'F':30},
	'D': {'G':60, 'H':20, 'A':20},
	'B': {'E':40, 'C':20},
	'F': {'C':30, 'E':50},
	'E': {'B':40, 'F':50,'I':10},
	'I': {'E':10, 'J':15},
	'K': {'H':40, 'J':10,  'G':30},
	'G': {'D':60, 'K':30},
	'H': {'D':20, 'K':40},
	'J': {'I':15, 'K':10},
}
dist={
	'A': sys.maxint,
	'C': sys.maxint,
	'D': sys.maxint,
	'B': sys.maxint,
	'F': sys.maxint,
	'E': sys.maxint,
	'I': sys.maxint,
	'K': sys.maxint,
	'G': sys.maxint,
	'H': sys.maxint,
	'J': sys.maxint,
	}

src='A'
dest='J'

def dij(graph, src, dest, dist):
	visited=[]
	parent={}
	parent[src]=None;
	
	q={}

	for key, val in dist.items():
		q[key]=val
	q[src]=0	
	
	dist[src]=0;

	while q:
		for w in sorted(q, key=q.get):
			temp=w
			del q[w]
			break

		print "dequed=", temp
		visited.append(temp)

		for i,val in graph[temp].iteritems():
			if i not in visited:
				if(dist[i]  >  val+dist[temp] ):
					dist[i]=val+dist[temp]
					parent[i]=temp
					q[i]=dist[i]


	print "shortest dist=", dist[dest]			
	k=dest


	while(parent[dest]!= None):
		print dest
		dest=parent[dest]
	print src	


	print visited
if __name__ == '__main__':
	dij(graph, src, dest, dist)