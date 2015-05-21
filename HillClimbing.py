from math import *
from random import *
from time import *
radius = 0.001
AREA = 100

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def generator():
	side = int(sqrt(AREA))
	for x in range(side):
		for y in range(side):
			yield(x,y)
def f(x, y):
	if x <= 0 or x >= 10 or y <= 0 or y >= 10:
		return float('inf')
	return x*sin(4*x) + 1.1*y*sin(2*y)

def hillClimbRandom():
	start = clock()
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	for i in range(100):
		x = random()*10
		y = random()*10

		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + radius*cos(t)
			trialY = y + radius*sin(t)
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
	return bestX, bestY, bestF
	print('Time = ', round(clock() - start, 1), 'seconds')

def HillClimbGrid():
	start = clock()
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	for coordinate in generator():
		x = coordinate[0]
		y = coordinate[1]

		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + radius*cos(t)
			trialY = y + radius*sin(t)
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
	return bestX, bestY, bestF
	print('Time = ', round(clock() - start, 1), 'seconds')

def lookup():
	x = random()*10
	y = random()*10
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	cosDict = dict()
	sinDict = dict()
	for t in frange(0, 2*pi, 2*pi/64):
		cosDict[t] = cos(t)
		sinDict[t] = sin(t)
	for a in range(100):
		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + radius*cosDict[t]
			trialY = y + radius*sinDict[t]
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
		x = bestX
		y = bestY
	return bestX, bestY, bestF

def allRandomEverything():
	start = clock()
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	for i in range(10000):
		x = random()*10
		y = random()*10
		for t in frange(0, 2*pi, 2*pi/64):
			trialX = x + radius*cos(t)
			trialY = y + radius*sin(t)
			trialF = f(trialX, trialY)
			if trialF < bestF:
				bestX = trialX
				bestY = trialY
				bestF = trialF
	return bestX, bestY, bestF
	print('Time = ', round(clock() - start, 1), 'seconds')

def nelderMead():
	bestX = float('inf')
	bestY = float('inf')
	bestF = float('inf')
	tot = []
	for trials in range(1000):
		tempList = [(random()*10, random()*10) for x in range(3)]
		temp = []
		for i in range(3):
			x = tempList[i][0]
			y = tempList[i][1]
			temp.append((f(x,y), x, y))
		temp.sort()
		A = temp[2]
		B = temp[0]
		C = temp[1]
		for index in range(100):
			M = midpoint(B, C)
			D = subtractVectors(addVectors(B,C), A)
			if D[0] < A[0]:
				E = subtractVectors(addVectors(multiplyVectorbyScalar(B, 1.5), multiplyVectorbyScalar(C, 1.5)), multiplyVectorbyScalar(A, 2))
				if E[0] < D[0]:
					A = E
				else:
					A = D
			else:
				F = subtractVectors(addVectors(multiplyVectorbyScalar(B, 0.75), multiplyVectorbyScalar(C, 0.75)), multiplyVectorbyScalar(A, 0.5))
				G = addVectors(addVectors(multiplyVectorbyScalar(B, 0.25), multiplyVectorbyScalar(C, 0.25)), multiplyVectorbyScalar(A, 0.5))
				if F[0] < A[0] or G[0] < A[0]:
					if F[0] < G[0]:
						A = F
					else:
						A = G
				else:
					H = midpoint(A, B)
					A = H
					C = M
		tot.append(A[0])
	tot.sort()
	return (tot[0])

def midpoint(v1, v2):
	newX = (v1[1] + v2[1])/2
	newY = (v1[2] + v2[2])/2
	newF = f(newX,newY)
	return ((newF, newX, newY))

def addVectors(v1, v2):
	newX = v1[1] + v2[1]
	newY = v1[2] + v2[2]
	newF = f(newX, newY)
	return ((newF, newX, newY))

def subtractVectors(v1, v2):
	newX = v1[1] - v2[1]
	newY = v1[2] - v2[2]
	newF = f(newX, newY)
	return ((newF, newX, newY))

def multiplyVectorbyScalar(v1, c):
	newX = v1[1] * c
	newY = v1[2] * c
	newF = f(newX, newY)
	return ((newF, newX, newY))
	
def main():
	start = clock()
	x1, y1, z1 = hillClimbRandom()
	print("Random: ")
	print(round(x1, 3), round(y1, 3), round(z1, 3))
	print('Time = ', round(clock() - start, 3), 'seconds')
	print()
	start1 = clock()
	x2, y2, z2 = HillClimbGrid()
	print("Grid: ")
	print(round(x2, 3), round(y2, 3), round(z2, 3))
	print('Time = ', round(clock() - start1, 3), 'seconds')
	print()
	start2 = clock()
	x3,y3,z3 = lookup()
	print("LookUp: ")
	print(round(x3, 3), round(y3, 3), round(z3, 3))
	print('Time = ', round(clock() - start2, 3), 'seconds')
	print()
	start3 = clock()
	x4,y4,z4 = allRandomEverything()
	print("Big Random: ")
	print(round(x4, 3), round(y4, 3), round(z4, 3))
	print('Time = ', round(clock() - start3, 3), 'seconds')
	print()
	start4 = clock()
	z5 = nelderMead()
	print("Nelder Mead: ")
	print(round(z5, 3))
	print('Time = ', round(clock() - start4, 3), 'seconds')



main()
