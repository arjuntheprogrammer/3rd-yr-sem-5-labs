def bottle():
	
	x=0
	y=0
	
	
	q=[]
	path=[]
	q.append([0,0])

	while q:
		temp=q.pop(0)
		print(" ")
		path.append(temp)
		x=temp[0]
		y=temp[1]
		if(y==4):
			print temp
			print("reached")
			break
		print("dequed:",temp, "=>")	
		if(x!=3 and ([3,y] not in  q) and ([3,y] not in  path) ):
			 q.append([3, y])
		if(y!=5 and ([x,5] not in  q) and ([x,5] not in  path) ):
			 q.append([x, 5])
		if(x==3 and ([0,y] not in  q) and ([0,y] not in  path)):
			 q.append([0, y])
		if(y==5 and ([x,0] not in  q) and ([x,0] not in  path)):
			 q.append([x, 0])

			
		if(x!=0 and y!=5):
			if(5-y >= x and ([0,y+x] not in  q) and ([0,y+x] not in  path)):
				 q.append([0, y+x])

			if(5-y<x and ([x-(5-y),5] not in  q) and ([x-(5-y),5] not in  path)):
				 q.append([x-(5-y), 5])

		if(x!=3 and y!=0):
			if(3-x >= y and ([x+y,0] not in  q) and ([x+y,0] not in  path)):
				 q.append([y+x, 0])

			if(3-x<y and ([3, y-(3-x)] not in  q) and ([3, y-(3-x)] not in  path)):
				 q.append([3, y-(3-x)])
		
		print  q		



if __name__ == '__main__':
	visited=[]
	
	print ("both empty")
	bottle()
