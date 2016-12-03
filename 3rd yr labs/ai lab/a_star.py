openl=[]
closel=[]

graph={
	'A': {'C':10, 'D':20},
	'C': {'A':10, 'B':20, 'F':30},
	'D': {'G':60, 'H':20, 'A':20},
	'B': {'E':40, 'C':20},
	'F': {'C':30, 'E':50},
	'E': {'B':40, 'F':50,'I':10},
	'I': {'E':10, 'J':15},
	'K': {'H':40, 'J':10, 'I':20, 'G':30},
	'G': {'D':60, 'K':30},
	'H': {'D':20, 'K':40},
	'J': {'I':15, 'K':10},
}

SLD={
	'A': 42,
	'C': 40,
	'D': 25,
	'B': 35,
	'F': 25,
	'E': 15,
	'I': 10,
	'K': 20,
	'G': 20,
	'H': 23,
	'J': 0,

}
Parent={
	
}

def a_star(start,goal, Parent, closel):
	Parentv={}
	ff={}
	openl=[start]
	closel=[]
	f=[0+SLD[start]]
	ff[start]=f[0]
	search=0
	Parent[start]=0
	Parentv[start]=None

	while openl and search==0:
		
		min1=min(f)
		i=f.index(min1)
		print "openl =" +`openl`
		print "f=" +`f`
		
		x=openl.pop(i)
		xf=f.pop(i)
		print "\ndequed=" + `x`+ "and f="+ `xf`

		for i, dic in graph[x].iteritems():
			if i not in closel:
				print "\nsuccessor of "+`x`+"=" + `i`+ "and value ="+ `dic`

				#Parent[i]= Parent[x]+dic
				#[i]=Parent[x]s
				if i==goal:	
					search=1

				F=Parent[x]+dic+SLD[i]
				print "parent of x="+ `Parent[x]` 
				print 'F of'+`i`+"="+ `F`
				#openl+=i
				#f+=Fs
				if i not in openl and i not in closel:
					Parent[i]= Parent[x]+ dic
					Parentv[i]=x
					openl+=i
					f.append(F)
					ff[i]=F
		
		#print "here"
		closel.append(x)
	closel.append(goal)	
	print closel
	print ""			
	print Parent
	print ""
	print ff
	print ""			
	print `Parentv`+"\n path="
	fun(Parentv, goal)
	
		
	
def fun(Parentv, x):
	if Parentv[x]==None:
		print (x)
		return 

	fun(Parentv, Parentv[x])
	print(x)	

		





if __name__ == '__main__':
	 a_star('A', 'J', Parent, closel)
	