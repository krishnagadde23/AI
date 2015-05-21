from random import choice, random, randrange, shuffle, sample
def main():
	doRandom()
	doSample()
	doChoice()
	doShuffle()
	doSeq()
def doRandom():
	r = random()
	if r > 0.5:
		print(1)
	else:
		print(-1)
def doSample():
	subSet = sample([-1,1], 1)
	print(subSet[0])
def doChoice():
	r = choice([-1,1])
	print(r)
def doShuffle():
	randList = [-1,1]
	shuffle(randList)
	print(randList[0])
def doSeq():
	seq = [-1,1]
	shuffle(seq)
	print(seq[0])

main()
