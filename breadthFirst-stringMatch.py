#	Will Kent-Daggett, Scott Hurlow, Aron Thomas
#	COMP-221 Algorithms
#	9/29/14
#	Programming #2/Question 1

"""Takes in a text string and a string representing a pattern of chars
to find in the text. Returns the index of the pattern's first match,
or -1 with no matches.
Also prints out verbose updates of its progress through the text, ie, 
the text, the pattern, the current index, and match/no match."""
def bfStringMatch(text, pattern):
	T = list(text)
	P = list(pattern)
	n = len(T)
	m = len(P)
	compCount = 0
	# print text
	# print pattern

	for i in range(0, n - m + 1):
		print "\nPos = ", i
		print text
		print textPointer(i, pattern)

		j = 0
		while (j < m):
			if (P[j] == T[i + j]):
				print textPointer(i + j, "^ Match!")
				compCount += 1
				j += 1
			else:
				print textPointer(i + j, "^ No match")
				compCount += 1
				break

		if j == m:
			print "\nPattern found at position ", i
			print "Total comparisons: ", compCount
			return i
	print "\nPattern not found"
	print "Total comparisons: ", compCount
	return -1

"""Helper function that takes in an int  and returns a string of spacer
spaces followed by the pointer"""
def textPointer(spacer, pointer):
	r = ""
	count = 0
	while count < spacer:
		r += " "
		count += 1
	r += pointer
	return r

text = input("Enter some text: ")
pattern = input("Enter a word to try and find in the text: ")
bfStringMatch(text, pattern)
# bfStringMatch("buy bo's elbow grease", 'bow')
