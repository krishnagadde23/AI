#
#-------------------------------------------------
# Krishna Gadde 9/11/14
# Stueben Period 1
# ------------------------------------------------
import pickle
#
def main():
	nbrs = pickle.load(open("isNbhrs.pkl", "rb"))
	path = []
	start = "sliver"
	finish = "silver"
	path, qCount = search(nbrs, start, finish, path)
	printSearch(path)
	print("The Count is: " + str(qCount))
#
#
#-------------------------------------------------
# prints the search in number form
#
def printSearch(path):
	count = 1
	for word in path:
		print(str(count) + ": " + word)
		count += 1
#
#
#--------------------------------------------------
# returns the path of the search in order
#
def returnPath(parentDict, start, finish):
	parent = ""
	temp = finish
	path = []
	path.append(finish)
	parent = parentDict[finish]
	while parent != None:
		path.append(parent)
		parent = parentDict[parent]
	path.reverse()
	return path
#
#
#-------------------------------------------------
# searches for the words in the path
#
#
def search(nbrs, start, finish, path):
	queue = []
	parentDict = {}
	wordList = {start : 0}
	popCount = 0
	gCount = 0
	queue.append((heuristic(start, finish), 0, start))
	parentDict[start] = None
	while len(queue) != 0:
		theFinalWord = queue.pop(0)
		current  = theFinalWord[2]
		gCount = theFinalWord[1]
		popCount += 1
		#wordList.append(current)
		for item in nbrs[current]:
			if item not in wordList or wordList[item] > gCount:
				if item == finish:
					parentDict[item] = current
					return returnPath(parentDict, start, finish), popCount
				queue.append((gCount + heuristic(item, finish), gCount + 1, item))
				parentDict[item] = current
				wordList[item] = gCount
		queue.sort()
#
#
#-------------------------------------------------
# Calculates the heuristic
#
#
def heuristic(word, end):
	counter = 0
	if word[0] != end[0]:
		counter += 1
	if word[1] != end[1]:
		counter += 1
	if word[2] != end[2]:
		counter += 1
	if word[3] != end[3]:
		counter += 1
	if word[4] != end[4]:
		counter += 1
	if word[5] != end[5]:
		counter += 1
	return counter
#
#
main()






