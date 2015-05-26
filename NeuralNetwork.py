from random import random, choice
from time import clock
TRIALS = 3000
ALPHA = 0.25
#INPUTS = [(0,0,-1,0), (0,1,-1,1), (1,0,-1,1), (1,1,-1,1)]
INPUTS2 = [(0,0,1,-1,0), (0,1,0,-1,1), (1,0,0,-1,1), (1,1,1,-1,0)]
SMALL = 0.4
#x = []
def dotProduct(v1, v2):
	return(v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])

def f(w, x):
	return int((w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + w[3]*x[3]) > 0)

def trained(w):
	#for x in INPUTS:
	for x in INPUTS2:
		if f(w, x) != x[3]:
			return False
	return True

def verifyNetwork(w, epochs):
	print(' Epochs = ', epochs)
	#for x in INPUTS:
	for x in INPUTS2:
		#t = x[3]
		t = x[4]
		y = f(w, x)
		print((y == t), t, x)
	m = round(-w[0]/w[1], 2)
	b = round(w[2]/w[1], 2)
	print("y = " + str(m) + "x + " + str(b))


def trainPerceptronWeights():
	w = [random()*2 - 1]*(len(INPUTS2) + 1)
	epochs = 0
	while epochs < TRIALS and not trained(w):
		#for x in INPUTS:
		for x in INPUTS2:
			#x = choice(INPUTS)
			x = choice(INPUTS2)
			#t = x[3]
			t = x[4]
			y = f(w, x)
			w[0] = w[0] - ALPHA*(y-t)*x[0]
			w[1] = w[1] - ALPHA*(y-t)*x[1]
			w[2] = w[2] - ALPHA*(y-t)*x[2]
			w[3] = w[3] - ALPHA*(y-t)*x[3]
		epochs += 1
	return w, epochs

def main():
	w, epochs = trainPerceptronWeights()
	verifyNetwork(w, epochs)
if __name__ == '__main__': START_TIME = clock(); main(); \
						   print('--> Run time = ', round(clock() - START_TIME, 2), 'seconds <--')

