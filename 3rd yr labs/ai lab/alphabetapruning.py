import math
import sys

branching=3
depth=3
heu_value=[]
index=0
tree=[]

def fill_heuristic_value(origin, depth):
	global index, branching
	if depth==0:
		tree[origin]=heu_value[index]
		index=index+1
		return
	for i in xrange(0, branching):
		fill_heuristic_value(branching*origin +i+1, depth-1)
		

def alphabeta(origin, depth, alpha, beta, maximising_player):	
	#print 'origin=', origin
	
	if depth==0:
		return tree[origin]

	if maximising_player:
		v=-sys.maxint-1
		for i in xrange(0, branching):
			v=max(v, alphabeta(branching*origin +i+1, depth-1, alpha, beta, False))
			alpha=max(alpha, v)
			if beta<=alpha and i!=branching-1:
				print 'at node=' ,origin, '=>beta cut off'
				break#beta cut off...
		tree[origin]=v		
		return v
	else :
		v=sys.maxint
		for i in xrange(0, branching):
			v=min(v, alphabeta(branching*origin +i+1, depth-1, alpha, beta, True))
			beta=min(beta, v)
			if beta<=alpha and i!=branching-1:
				print 'at node=' ,origin, '=>alpha cut off'
				break #alpha cut off...
		tree[origin]=v
		return v					

if __name__ == '__main__':
	origin=0
	depth

	for i in xrange(0, int((math.pow(branching,depth+1)-1)/(depth-1)) ):
		tree.append('$')

	# heu_value.append(-4)
	# heu_value.append(-8)
	# heu_value.append(-2)
	# heu_value.append(20)
	# heu_value.append(11)
	# heu_value.append(18)
	# heu_value.append(14)
	# heu_value.append(-4)

	# heu_value.append(-16)
	# heu_value.append(4)
	# heu_value.append(18)
	# heu_value.append(-11)
	# heu_value.append(-11)
	# heu_value.append(-6)
	# heu_value.append(3)
	# heu_value.append(8)

	heu_value.append(-10)
	heu_value.append(20)
	heu_value.append(11)
	heu_value.append(-3)
	heu_value.append(-18)
	heu_value.append(13)
	heu_value.append(-12)
	heu_value.append(-12)
	heu_value.append(19)
	heu_value.append(2)
	heu_value.append(13)
	heu_value.append(4)
	heu_value.append(-18)
	heu_value.append(-18)
	heu_value.append(11)
	heu_value.append(0)
	heu_value.append(15)
	heu_value.append(15)
	heu_value.append(-2)
	heu_value.append(4)
	heu_value.append(13)
	heu_value.append(11)
	heu_value.append(-16)
	heu_value.append(-5)
	heu_value.append(6)
	heu_value.append(7)
	heu_value.append(19)

	fill_heuristic_value(origin, depth)
	

	alphabeta(origin, depth,-sys.maxint-1, sys.maxint, True)
	print ""
	for i,j in enumerate(tree):
		print  'value at node ',i,'=>',j
		
	
