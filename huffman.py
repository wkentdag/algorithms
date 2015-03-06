import random
import heapq

def makeEmptyTree():
    return []

def makeLeaf(leafVal):
    return [leafVal, [], []]

def getNodeValue(tree):
    return tree[0]
def getLeftChild(tree):
    return tree[1]
def getRightChild(tree):
    return tree[2]

def addLeftChild(tree, subtree):
    tree[1] = subtree
    
def addRightChild(tree, subtree):
    tree[2] = subtree
       
def isLeaf(tree):
    return tree[1] == [] and tree[2] == []

def printTree(tree):
    printTreeRec(tree, 0)
       
def printTreeRec(tree, depth):
    if tree == []:
        print ' ' * depth, "Empty Tree"
    elif isLeaf(tree):
        print ' ' * depth, "Leaf:", tree[0]
    else:
        print ' ' * depth, "Node:", tree[0]
        print ' ' * depth, "Left subtree:"
        printTreeRec(tree[1], depth+4)
        print ' ' * depth, "Right subtree:"
        printTreeRec(tree[2], depth+4)
#===================================================

def makeRandomString(l):
	"""returns an l-length random string of lowercase ascii letters"""
	s = ''
	# generate random ascii char from int, append to s
	for i in range(l):
		n = random.randint(97, 122)
		c = str(unichr(n))
		s += c
	print 'String to encode:\t', s
	return s

def makeFrequencyTable(s):
	"""takes in a string s, and returns a minheap of tuples with each distinct letter and its frequency"""
	s = list(s)
	d = {}
	l = []

	# record values into a dict
	for i in range(len(s)):
		if s[i] not in d:
			d.update({s[i]:1})
		else:
			d[s[i]] += 1

	# sort the dict's k:v into tuples in a minheap, return
	for key in d:
		heapq.heappush(l, (d[key], key))

	print 'Frequency table:\t', l
	return l

def huffmanBuilder(C):
	"""takes in a frequency table and returns a huffman tree"""
	Q = []
	n = len(C)

	for c in C:
		heapq.heappush(Q, makeLeaf(c))

	for i in range(n-1):
		x = heapq.heappop(Q)
		y = heapq.heappop(Q)

		# get z's priority from x+y, make new node
		zP = x[0][0] + y[0][0]
		z = makeLeaf((zP, '*'))

		# make z,x,y a subtree, append to Q
		addLeftChild(z, x)
		addRightChild(z, y)
		heapq.heappush(Q, z)

	printTreeRec(Q[0], 8)
	return Q[0]

def huffmanEncoder(s, t):
	"""encodes string s with Tree t"""
	s = list(s)
	b = []
	for i in range(len(s)):
		val = recursiveHuff(t, '', s[i])
		# print 'val:', val, '\n'
		b.append(val)
	# print b

def recursiveHuff(tree, path, char):
	"""given a tree, an empty string 'path', and a character,
	finds said char in tree and returns the binary path"""
	# print 'looking for:\t', char, 'path:\t', path
	if isLeaf(tree):
		n = getNodeValue(tree)
		if n[1] == char:
			print 'found', char, 'at', path
			return path
	else:
		recursiveHuff(getLeftChild(tree), path+'0', char)
		recursiveHuff(getRightChild(tree), path+'1', char)

def decodeHuffman(b, t):
	"""takes in a binary string, and a tree, returns the decoded string """
	d = ''
	node = t

	# while p < len(b):
	# 	while not isLeaf(node)
	# 		for i in b:
	# 			if i == '0':
	# 				node = getLeftChild(node)
	# 			else:
	# 				node = getRightChild(node)
	# 	d.append(node[0][1])

	for i in b:
		if isLeaf(node):
			d += node[0][1]
			node = t
		elif i == '0':
			node = getLeftChild(node)
		else:
			node = getRightChild(node)

		# print d
	print d
	return d

mac = [(1, 'm'), (1, 's'), (1, 'o'), (1, 'g'), (2, 'a'), (2, 'c'), (3, 'l'), (4, 'e')]
# huffmanBuilder(mac)
m = 'macalestercollege'
# huffmanEncoder(m, huffmanBuilder(mac))
x = huffmanBuilder(mac)
# recursiveHuff(x, '', 0)
huffmanEncoder(m, x)
# lc = getLeftChild(x)
# print 'xxxxxxx', lc[0][0]
decodeHuffman('01011001010001000110011100', x)






