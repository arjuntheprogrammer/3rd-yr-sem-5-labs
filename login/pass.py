pas = open("pass1.txt", "w")
pas.write("[")

#ch=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
for i in range(97, 123):
	for j in range(0,10):
		for k in range(97, 123):
			pas.write("'"+chr(i)+chr(i)+`j`+`j`+chr(k)+chr(k)+"', ")


for l in range(0,10):
	for m in range(97, 123):
		for n in range(0, 10):
			pas.write("'"+ `l`+`l`+chr(m)+chr(m)+`n`+`n`+"' , ")


pas.write("]")

