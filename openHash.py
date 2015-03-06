"""
Open Hash Table implementation in Python.
Run openHash.py in python 2.7 to start user build.
The HashTable class supports inserting of integer and string values.
printTable method shows full table with current values.
HashTable class also depends on the deque data structure provided in python
collections. Deque functions as an efficient linkedlist-like data structure
to hold the values at a hiven hash index in the hash table.

by Scott Hurlow and Will Kent-Daggett"""


from collections import deque

def hashInt(x, m):
  return abs(x) % m

def hashStr(s, m):
  h = 0
  for c in s:
    h = ( 4*h + ord(c) ) % m
  return h

class HashTable():
  """Implementation of open-hashing HashTable in python 2.7"""

  def __init__(self, size):
    self.data = [ deque() for i in range(size) ]
    self.size = size


  def insert(self, x):
    if type(x) == int:
      hash = hashInt
    elif type(x) == str:
      hash = hashStr

    h = hash(x, self.size)
    linklist = self.data[h]
    linklist.appendleft(x)


  def printTable(self):
    print '\nHash Index | Value\n============'


    for i in xrange(0,self.size):
      ll = self.data[i]
      print i,
      for e in ll:
        print '['+ str(e) +']',
      print '\n---'

    print '============\n'



def buildHT():
  tableSize = input('Enter hashtable size: ')

  HT = HashTable(tableSize)

  for x in xrange(1, tableSize):
    val = input('\nAdd value: ')
    if val < 0:
      print 'exit'
      return 'done'
    HT.insert(val)
    HT.printTable()


buildHT()