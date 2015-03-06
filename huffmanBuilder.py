import random

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

def makeString(l):
	s = ''
	for i in range(l):
		n = random.randint(97, 122)
		# print 'n:\t',n
		c = str(unichr(n))
		# print 'c:\t', c, '\n'
		s += c
	print s
	return s

def makeFrequencyTable(s):
	s = list(s)
	d = {}
	l = Q.PriorityQueue()

	for i in range(len(s)):
		if s[i] not in d:
			d.update({s[i]:1})
		else:
			d[s[i]] += 1
	# print d
	for key in d:
		# print key, d[key]
		l.put((d[key], key))

	while not l.empty():
	    print l.get(),

	return l

def huffman(C):
	q = Q.PriorityQueue()
	n = C.qsize()
	print 'n', n
	for c in C:
		print C[c]

s = makeString(20)
t = makeFrequencyTable(s)
huffman(t)