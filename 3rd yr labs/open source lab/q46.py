f1=open("file.txt", "r")
words=[]
j=0
for line in f1:
	words.append(line.rstrip())

for word in words:
	j+=1
	if(j==50):
		break

	print "*********************\n"+word
	w1=""
	w2=""

	for i in range(0, len(word)):
		if(i%2==0):
			w1+=(word[i])
	
	for i in range(0, len(word)):
		if(i%2==1):
			w2+=(word[i])		
	print "w1="+w1
	print "w2="+w2

	if w1 in words:
		print w1
	if w2 in words:
		print w2		
