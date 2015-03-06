#	Will Kent-Daggett, Aron Thomas, Scott Hurlow
#	COMP-221 Algorithms
#	Programming 4, Question 1 (Heap construction)
###################################################

import random
import timeit

def heapify(h):
	"""Takes in a sortable array h;
	returns h sorted as a max-heap by the bottom-up heap method;
	prints completion time;"""
	print 'Generating', len(h), 'node heap...'
	start = timeit.default_timer()
	n = len(h) -1
	mid = n // 2 -1

	for i in range(mid, -1, -1):
		k = i 			# k = loop/array index
		v = h[k] 		# v = value of h[k]
		heap = False

		while not heap and 2 * k +1 <= n:
			j = 2 * k + 1
			if j < n: 	# there are 2 children
				if h[j] < h[j+1]:
					j = j+1
			if v >= h[j]:
				heap = True
			else:
				h[k] = h[j]
				k = j
		h[k] = v

	stop = timeit.default_timer()
	print 'Generated', len(h), 'node heap in:', stop-start, 'seconds\n'

def randomArray(l):
	"""Takes in an int l;
	returns an array, length l, of numbers such that 0 < n < l;"""
	r = []
	for i in range(0,l):
		r.append(random.randint(0, 20))
	return r

def generateHeaps(n):
	"""performs heapify(3+2^n) n times;
	the array is generated using randomArray(x),
	where x starts at 3"""
	i = 0
	x = 3
	while i < n:
		heapify(randomArray(x))
		x = 2 * x + 1
		i += 1

generateHeaps(10)