import random
import string
import time

guyprefers = {
 	'dan': ['abi', 'eve', 'ivy', 'meg'],
 	'abe': ['eve', 'ivy', 'abi', 'meg'],
 	'ned': ['abi', 'meg', 'ivy', 'eve'],
 	'sam': ['ivy', 'abi', 'meg', 'eve'],
}

girlprefers = {
	'abi': ['dan', 'ned', 'abe', 'sam'],
	'eve': ['ned', 'sam', 'abe', 'dan'],
	'ivy': ['sam', 'abe', 'ned', 'dan'],
	'meg': ['sam', 'dan', 'ned', 'abe'],
}


guys = guyprefers.keys();
girls = girlprefers.keys();

def stableMarriage(guys, girls, guyprefers, girlprefers):
	pairs = [];
	freeGuys = guys;
	freeGirls = girls;
	while len(freeGuys) > 0:
		currGuy = guys[0];
		prefsGuy = guyprefers.get(currGuy);
		currGirl = prefsGuy[0];
		prefsGirl = girlprefers.get(currGirl);
		print (currGuy + " proposes to " + currGirl)
		if currGirl in freeGirls:
			print(currGirl + " accepts")
			pairs.append((currGuy,currGirl));
			freeGuys.remove(currGuy);
			freeGirls.remove(currGirl);
		else:
			print('conflict')
			for girl in range(0,len(pairs)): # For loop looks through tuple pairs to find name of guy in pair
				if currGirl in pairs[girl]:
					currPair = pairs[girl]
					otherGuy = currPair[0];
			print(currGirl + " is already married to " + otherGuy)
			if prefsGirl.index(currGuy) < prefsGirl.index(otherGuy): # if girl prefers proposing guy to her current partner
				print(currGirl + " leaves " + otherGuy + " for " + currGuy)
				pairs.remove(currPair);
				freeGuys.append(otherGuy);
				freeGuys.remove(currGuy);
				prefsGuy.remove(currGirl)
				guyprefers[currGuy] = prefsGuy
				pairs.append((currGuy,currGirl));
			else:
				print(currGirl + " refuses the proposal")
				prefsGuy.remove(currGirl)
				guyprefers[currGuy] = prefsGuy
	return(pairs)




####
def testStableMarriage():
	size = input("enter the number of pairs you want: ");
	guyList = []
	girlList = []
	guyPrefs = {}
	girlPrefs = {}
	for i in range(0,size):
		letter = random.choice(string.letters)
		guyList.append(letter)
		letter = random.choice(string.letters)
		girlList.append(letter)
	for j in range(0,size):
		entry = girlList[j]
		list1 = guyList
		random.shuffle(list1)
		girlPrefs[entry] = list1
	for j in range(0,size):
		entry = guyList[j]
		list2 = girlList
		random.shuffle(list2)
		guyPrefs[guyList[j]] = list2
	start_time = time.time()
	stableMarriage(guyList,girlList,guyPrefs,girlPrefs)	
	total = time.time() - start_time
	print(str(total) + " seconds elapsed")



testStableMarriage()

