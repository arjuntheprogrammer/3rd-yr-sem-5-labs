pas = open("passalg.txt", "w")
pas.write("[")

a1=['1','2','3','4','5','6','7','8','9','0']
a2=['q','w','e','r','t','y','u','i','o','p']
a3=['a','s','d','f','g','h','j','k','l','l']

#121
#212
#112
#211

#221
#122


#123
#213
#312


i1=-1
for i in a2:
	i1+=1
	j1=-1
	for j in a2:
		j1+=1
		k1=-1

		for k in a1:
			k1+=1
			
			if j==i:
				continue
			ind=[i1, j1, k1]
			ind.sort()
			if ((ind[2]-ind[0])<=2 ):
				pas.write("'"+ i + i + j + j + k + k + "', ")
							
"""
	j1=-1
	for j in a3:
		j1++
		k1=-1

		for k in a1:
			if k==i:
				continue
			k1++
			ind=[i1, j1, k1]
			ind.sort()
			if abs(ind[0]-ind[2]<=-2)
				pas.write("'"+ i + i + j + j + k + k + "', ")
	
	
	
"""

################################################

i1=-1
for i in a1:
	i1+=1
	j1=-1
	for j in a2:
		j1+=1
		k1=-1

		for k in a2:
			k1+=1
			
			if j==k:
				continue
			ind=[i1, j1, k1]
			ind.sort()
			if ((ind[2]-ind[0])<=2):
				pas.write("'"+ i + i + j + j + k + k + "', ")
							
"""
	j1=-1
	for j in a3:
		j1++
		k1=-1

		for k in a1:
			if k==i:
				continue
			k1++
			ind=[i1, j1, k1]
			ind.sort()
			if abs(ind[0]-ind[2]<=-2)
				pas.write("'"+ i + i + j + j + k + k + "', ")
	
	




"""