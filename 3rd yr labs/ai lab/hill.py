from __future__ import print_function
########################
def displaced(start, goal):
	xx=0  #no of disp. tiles
	for i in xrange(3):
		for j in xrange(3):
			
			""" 
			#by displaced tiles
			#if start[i][j]!=' '  and start[i][j]!=goal[i][j]:
			#	xx+=1
			"""

			"""
			#by manhatan distance
			if(start[i][j]!=' '):
				f=0;		
				for ii in xrange(3):
					for jj in xrange(3):
						if(goal[ii][jj]==start[i][j]):
							xx+=abs(i-ii)+abs(j-jj)

							#print("coor:", i, j," ", ii, jj)
							#print("diff=", abs(i-ii)+abs(j-jj))
							#print ("xx=", xx)
							f=1
							break					
					if f==1:
						break		
			"""
	return xx			


def cop(src, dest):
	for i in xrange(3):
		for j in xrange(3):
			dest[i][j]=src[i][j]

########################
#bx, by=indicies of free space.
def hill(start, goal, bx, by):

	print("")
	print("")	
	print(start)
	dis=displaced(start, goal)
	print("displaced=", dis)
	print("bx=",bx, "by=", by)
	
	min1=dis
	patt1=[[0 for x in range(3)] for y in range(3)] 
	patt2=[[0 for x in range(3)] for y in range(3)]
	patt3=[[0 for x in range(3)] for y in range(3)]
	patt4=[[0 for x in range(3)] for y in range(3)]
	
	#start1=[]
	#cop(start, start1)

	if(min1==0):
		print ("goal reached")
		return 

	else:
		f=-1
		mins=[]
		m=dis
		if(by>0):	
			cop(start,patt1)
			patt1[bx][by]=patt1[bx][by-1]
			patt1[bx][by-1]=' '
			
			temp=displaced(patt1,goal)
			#print("patt1=\n", patt1, "\ntemp=", temp)
			
			if(min1>temp):
				min1=temp
				f=1	

		if(bx>0):	
			cop(start,patt2)
			patt2[bx][by]=patt2[bx-1][by]
			patt2[bx-1][by]=' '
			
			temp=displaced(patt2,goal)
			#print("patt2=\n", patt1, "\ntemp=", temp)
			if(min1>temp):
				min1=temp
				f=2
		if(by<2):
			cop(start,patt3)
			patt3[bx][by]=patt3[bx][by+1]
			patt3[bx][by+1]=' '
			
			temp=displaced(patt3,goal)
			#print("patt3=\n", patt1, "\ntemp=", temp)
			if(min1>temp):
				min1=temp
				f=3

		if(bx<2):	
			cop(start,patt4)
			patt4[bx][by]=patt4[bx+1][by]
			patt4[bx+1][by]=' '	
			
			temp=displaced(patt4,goal)
			#print("patt4=\n", patt1, "\ntemp=", temp)
			if(min1>temp):
				min1=temp
				f=4

		print("f=",f)		
		if(min1==dis):
			print ("goal cant be reached")
		
		else:
			if(f==1):
				#print (patt1)
				hill(patt1, goal, bx, by-1)
			elif(f==2):
				#print (patt2)
				hill(patt2, goal, bx-1, by)
			elif(f==3):
				#print (patt3)
				hill(patt3, goal, bx, by+1)
			elif(f==4):
				#print (patt4)
				hill(patt4, goal, bx+1, by)
			

##########################
"""
start=[]

start.append([])
start.append([])
start.append([])

start[0].append(6)
start[0].append(5)
start[0].append(3)


start[1].append(1)
start[1].append(4)
start[1].append(7)


start[2].append(8)
start[2].append(2)
start[2].append(' ')



goal=[]

goal.append([])
goal.append([])
goal.append([])

goal[0].append(1)
goal[0].append(2)
goal[0].append(3)


goal[1].append(4)
goal[1].append(5)
goal[1].append(6)


goal[2].append(7)
goal[2].append(8)
goal[2].append(' ')

"""

start=[]

start.append([])
start.append([])
start.append([])

start[0].append(2)
start[0].append(8)
start[0].append(3)


start[1].append(1)
start[1].append(6)
start[1].append(4)


start[2].append(7)
start[2].append(' ')
start[2].append(5)



goal=[]

goal.append([])
goal.append([])
goal.append([])

goal[0].append(1)
goal[0].append(2)
goal[0].append(3)


goal[1].append(8)
goal[1].append(' ')
goal[1].append(4)


goal[2].append(7)
goal[2].append(6)
goal[2].append(5)












hill(start, goal, 2,1)


"""
for i in xrange(3):
	for j in xrange(3):
		print(goal[i][j], end="")
	print("")	
"""	

