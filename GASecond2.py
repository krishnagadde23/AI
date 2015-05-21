#############################################
# Krishna Gadde        						#
# Period 1          						#
# April 7, 2015         					#
# GASecond2          						#
#############################################
MAX = 20
POP = 200

from random import *
from math import *
def cost(x, y):
	return x*sin(4*x) + 1.1*y*sin(2*y)

def createPopulation():
	M = [''.join([str(randint(0,1)) for c in range(MAX)]) for r in range(POP)]
	return M

def printMatrix(martix):
	for row in martix:
		for col in row:
			print(col, end = '  ')
		print('')

def allSame(matrix):
	curr = matrix[0]
	for row in matrix:
		if curr != row:
			return False
	return True

def main():
	pop = createPopulation()
	boolean = False
	z = 0
	for i in range(POP):
		H = len(pop[i])//2
		x = int(pop[i][0:H], 2)/(102.3)
		y = int(pop[i][H: ], 2)/(102.3)
		pop[i] = (cost(x, y), pop[i])
	while boolean == False:
		newPop = []
		for i in range(POP):
			H = len(pop[i][1])//2
			x = int(pop[i][1][0:H], 2)/(102.3)
			y = int(pop[i][1][H: ], 2)/(102.3)
			pop[i] = (cost(x, y), pop[i][1])
		pop.sort()
		#pop.reverse()
		for i in range(1, (len(pop)//2) + 1):
			par1 = pop[0]
			par2 = pop[i]
			r = randint(1,9)
			ch1 = par1[0:r] + par2[r:]
			ch2 = par2[0:r] + par1[r:]
			newPop.append(ch1)
			newPop.append(ch2)
		pop = newPop
		z += 1
		boolean = allSame(pop)
		print(' Generation ' + repr(z))
		printMatrix(pop)

main()
