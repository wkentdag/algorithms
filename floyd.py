#	Will Kent-Daggett + Scott Hurlow
#	COMP-221 Algorithms
#	Programming 5, Question 4 (Floyd's Algorithm)
###################################################

import random
import timeit

def floyd(a, p):
	"""Takes in an adjacency matrix a, and performs floyd's 
	algorithm for shortest pairs, returning time elapsed. 
	Also takes in a boolean p, which, if True, 
	prints the matrix before and after as well as the
	elapsed time. Returns elapsed time."""
	if p:
		print 'a:'
		for elem in a:
			print "\t".join([str(val) for val in elem])
		print "\n"

	start = timeit.default_timer()
	n = len(a)

	for k in range(n):
		for i in range(n):
			for j in range(n):
				a[i][j] = min(a[i][j], a[i][k] + a[k][j])
				
	stop = timeit.default_timer()

	if p:
		print 'after applying floyds algorithm:'
		for elem in a:
			print "\t".join([str(val) for val in elem])
		print "\n"
		print 'Found shortest pairs in', stop-start, 'seconds\n'
	return stop-start

def random2dGraph(a, b):
	"""Generates an AxA 2d array with random values within range 1 - b
	When the random value = b, it becomes inf"""
	m = [[0 for x in range(a)] for x in range(a)]
	for i in range(0, a):
		for j in range(0, a):
			if (j == i):
				m[i][j] = 0
			else:
				r = random.randint(1, b)
				if (r == b):
					r = float("inf")
				m[i][j] = r
	return m

def bigTests(a, b, c):
	"""Runs floyd() A times on BxB-sized matrices,
	populated with random values ranging from 1-c.
	Returns and prints the average completion time.
	floyd()'s 'p' variable is set to false by default for
	easily readable output"""
	s = 0
	for i in range(a):
		s += floyd(random2dGraph(b, c), False)
	print 'Average time for', a, b, 'x', b, 'graphs:\t', s / a
	return s / a

################################################### main:
inf = float("inf")
hwExample = [[0, inf, 8, 20, inf], [5, 0, inf, 9, inf], [10, inf, 0, 6, 12], [20, inf, 6, 0, 3], [inf, 2, 12, 3, 0]]

print "An example from the homework:\n"
floyd(hwExample, True)

print "Average results from several large trials:\n"
bigTests(10, 10, 10)
bigTests(10, 20, 10)
bigTests(10, 40, 10)
bigTests(10, 80, 10)
bigTests(10, 160, 10)

