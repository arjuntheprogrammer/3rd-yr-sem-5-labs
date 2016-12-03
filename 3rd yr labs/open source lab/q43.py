from collections import defaultdict
def fun():
	f1=open("file.txt", 'r')
	words=[]
		
	for line in f1:
		words.append(line.rstrip())
		print words


	diction=defaultdict(list)
	
	for word in words:
		key= "".join(sorted(word))
		#print "key="+ `key`
		diction[key].append(word)


	longest=0
	for word, lis in diction.items():
		if len(lis)>longest:
			longest=len(lis)

	for i, j in diction.items():
		if len(j)>longest-1:
			print i, j		 


if __name__ == '__main__':
	fun()
