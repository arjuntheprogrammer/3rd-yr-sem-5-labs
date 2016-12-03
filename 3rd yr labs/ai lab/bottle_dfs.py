def bottle(x, y, visited, level):
	level+=1
	temp=[x,y]

	if(y==4):
		print ("\n destination reached")
		return True
	

	if(temp in visited):
		print "already visited"
		return False
	
	else:
		visited.append(temp)
		
		if(x==0):
			#x=3;
			print ("3",`y`, "  fill x", " level=", level)
		
			if(bottle(3,y, visited, level)==True):
			#	x=0;
			#else:
				return True;

						
		if(x>0 and y!=5):
			if(5-y>=x):
				
				#y+=x
				#x=0				
				print ("0",`y+x`, "  fill y with x", " level=", level)
		
				if(bottle(0, y+x, visited, level)==True):
				#	x=0;
				#else:
					return True;
			

			else :	
				x-=5-y
				y=5
				print (`x-(5-y)`,"5", "  fill y with x", " level=", level)
		
				if(bottle(x-(5-y), 5, visited, level)==True):
					return True

		if(x>0 and y==5):
			#y=0;
			print (`x`,"0", "  empty y", " level=", level)

			if(bottle(x, 0, visited, level)==True):
				return True
				
	return False			
 


if __name__ == '__main__':
	visited=[]
	level=0
	print ("both empty")
	bottle(0, 0, visited, 0)
