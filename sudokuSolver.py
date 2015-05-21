#############################################
#     Name: Krishna Gadde                   #
#     Period: 1                             #
#     Date: 11/18/14                        #
#                                           #
#     Description:                          #
#     Solves the Sudoku Puzzle				#
#	  Uses a recursive Sudoku method		#
#############################################
import copy
from time import clock
import math

def printGrid(grid):
	for i in range(0, len(grid)):
		print(grid[i])

def appendTheNeighbors(grid, nbrs):
	for i in range(0, N):
		grid.append([])
		for j in range(0, N):
			grid[i].append(line[i*N+j])
			if (grid[i][j] == '.'):
				locs[i*N+j] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
			nbrs[i*N+j] = []
			for k in range(0, N):
				nbrs[i*N+j].append(k*N+j)
				nbrs[i*N+j].append(i*N+k)
				nbrs[i*N+j].append((i//3*3 + k//3)*N + j//3*3 + k%3)
			while(i*N+j in nbrs[i*N+j]):
				nbrs[i*N+j].remove(i*N+j)
def checkForNeighbors(grid, nbrs):
	for index in nbrs.keys():
		x = index//N
		y = index%N
		for i in nbrs[index]:
			if grid[x][y] == grid[i//N][i%N] or grid[x][y] == '.':
				return False
	printGrid(grid)
	return True

def solvetheSoduku(grid, locs, nbrs):
	index = -1
	cur = 9
	for i in locs.keys():
		if len(locs[i]) == 0 and grid[i//N][i%N] == '.':
			return
		if 0 < len(locs[i]) <= cur:
			index = i
			cur = len(locs[i])
	if index == -1:
		checkForNeighbors(grid, nbrs)
		return
	x = index//N
	y = index%N
	for elem in locs[index]:
		grid[x][y] = elem
		temp = locs[index]
		locs[index] = []
		removed = []
		for i in nbrs[index]:
			if i in locs.keys():
				if elem in locs[i]:
					removed.append(i)
					locs[i].remove(elem)
		solvetheSoduku(grid, locs, nbrs)
		locs[index] = temp
		for i in removed:
			locs[i].append(elem)
		grid[x][y] = '.'
	return

def updateTheSudoku(grid, locs, nbrs):
	for key in locs.keys():
		x = key//N
		y = key%N
		for i in nbrs[key]:
			if (grid[i//N][i%N] in locs[x*N+y]) and (grid[i//N][i%N] != '.'):
				locs[x*N+y].remove(grid[i//N][i%N])
	return

def main():
	return
start = clock()
line = input("Please enter the puzzle (enter exit to quit):\n")
while (line != "exit"):
	N = (int)(math.sqrt(len(line)))
	grid = []
	locs = {}
	nbrs = {}
	appendTheNeighbors(grid, nbrs)
	updateTheSudoku(grid, locs, nbrs)
	solvetheSoduku(grid, locs, nbrs)
	print('Time = ', round(clock() - start, 2), 'seconds')
	line = input("Please enter the puzzle (enter exit to quit):\n")
	start = 0

main()

