
from collections import defaultdict

def anagram_finder(file_name):

	# We first get each word from the file
	words = []
	with open(file_name, 'r') as f:
		for line in f:
			words.append(line.rstrip())

	# The point here is that every word that have the same letters and the
	# same length will be the same when they are sorted
	# For a good enough explanation of defaultdict, see this answer:
	# http://goo.gl/NbwXOv or in your Python interpreter, do:
	# >> help('collections.defaultdict')
	# If you know how defaultdict works, you should understand this
	# block of codes
	anadict = defaultdict(list)
	for word in words:
		key = ''.join(sorted(word))
		anadict[key].append(word)

	# We then get the words length of the anagrams with the most words in 
	# them
	longestana = 0
	for anagram, anawords in anadict.items():
		if len(anawords) > longestana:
			longestana = len(anawords)

	# We could shorten the above block like so, but the one above runs faster
	# longestana = max(map(lambda x: len(anadict[x]), anadict))

	# And finally, we print only the anagrams with the most words in them
	for anagram, anawords in anadict.items():
		#if len(anawords) > longestana-1:
		print anagram, anawords

#test
anagram_finder('file.txt')