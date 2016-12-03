
from random import randrange

def brackets(n):
	i, result, brackets = 0, '', '[]'
	j=0
	ans=1
	a1='['
	a2=']'
	while i < n*2:

		result += brackets[randrange(len(brackets))]
		if(result[i] is a1):
			j+=1
		else:
			j-=1
		if j<0:
			ans=0;


		i+=1
		

	if ans==1 and j==0:
			print result, 'OK'
	else:
		print result, 'NOT OK'
				
#test
brackets(3)