from itertools import permutations
from pickle import dump, load
from random import *
from math import ceil, floor

def main():
	database =  loadDatabase()
	for x in range(100000):
		computerLearning(database)
	saveDatabase(database)
	HumanTurn(database)
	print(database)


def weightedProb(lst):
	prob = randint(1, sum(lst))
	i = -1
	while prob > 0:
		i = i + 1
		prob = prob - lst[i]
	return i

def stringBoard(perm, limit):
	newBoard = '---------'
	for n in range(limit+1):
		if n % 2 == 0:
			newBoard = insertX(newBoard, perm.index(n))
			yield newBoard
		else:
			newBoard = insertO(newBoard, perm.index(n))
			yield newBoard

def insertX(newBoard, index):
	newBoard = newBoard[:index] + 'X' + newBoard[(index + 1):]
	return newBoard

def insertO(newBoard, index):
	newBoard = newBoard[:index] + 'O' + newBoard[(index + 1):]
	return newBoard

def win(board):	
	if board[0] == board[1] == board[2] != '-':
		return board[0]
	if board[3] == board[4] == board[5] != '-':
		return board[3]
	if board[6] == board[7] == board[8] != '-':
		return board[6]
	if board[0] == board[3] == board[6] != '-':
		return board[0]
	if board[1] == board[4] == board[7] != '-':
		return board[1]
	if board[2] == board[5] == board[8] != '-':
		return board[2]
	if board[0] == board[4] == board[8] != '-':
		return board[0]
	if board[2] == board[4] == board[6] != '-':
		return board[2]
	return False

def makeDatabase():
	sequence = [0,1,2,3,4,5,6,7,8]
	filledBoards = list(permutations(sequence, 9))
	database = {'---------':[1 for x in range(9)]}	
	for perm in filledBoards:
		limit = 0
		board = stringBoard(perm,limit)
		while(limit < 9 and not isWin(board) and not isTie(board)):
			database[board] = [1 if board[x] == '-' else 0 for x in range(9)]
			limit += 1
			board = stringBoard(perm,limit)
	saveDatabase(database)
	print(len(database))

def saveDatabase(database):
	fout = open( 'database.pkl' , 'wb' ) 	
	dump( database , fout , protocol = 2 )
	fout.close()

def loadDatabase():
	database = load( open( 'database.pkl' , 'rb' ) )
	return database

	return False

def computerLearning(database): #X goes first
	board = '---------'
	turn = 0 
	gameSet = []
	while (not win(board) and not draw(board)):
		#print(board)
		loc = weightedProb(database[board])
		gameSet.append([board,loc])
		if turn%2 == 0: #X
			board = insertX(board, loc)
		else:
			board = insertO(board, loc)
		turn = turn + 1

	# gameSet.remove([board, turn-1])
	# print gameSet
	winner = win(board)
	# print winner
	if winner == 'X':
		for x in range(len(gameSet)/2+1):
			i = 2*x
			database[gameSet[i][0]][gameSet[i][1]] += 3
		database[gameSet[i][0]] = [0,0,0,0,0,0,0,0,0]
		database[gameSet[i][0]][gameSet[i][1]] = 1
		for x in range(len(gameSet)/2):
			i = 2*x
			database[gameSet[i+1][0]][gameSet[i+1][1]] = int(ceil(database[gameSet[i+1][0]][gameSet[i+1][1]]/2.0))
	elif winner == 'O':
		for x in range(len(gameSet)/2):
			i = 2*x
			database[gameSet[i][0]][gameSet[i][1]] = int(ceil(database[gameSet[i][0]][gameSet[i][1]]/2.0))
			database[gameSet[i+1][0]][gameSet[i+1][1]] +=3
		database[gameSet[i+1][0]] = [0,0,0,0,0,0,0,0,0]
		database[gameSet[i+1][0]][gameSet[i+1][1]] = 1
	else:
		for x in range(len(gameSet)):
			database[gameSet[x][0]][gameSet[x][1]] += 1

def draw(board):
	if '-' not in board and not (win(board, 'X') or win(board, 'O')):
		return True
	return False

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def HumanTurn(database):
	board = '---------'
	turn = 0 #evens are X's turn; odds are O's turn
	gameSet = []
	while (not win(board) and not draw(board)):
		gameSet.append(board)
		drawBoard(board)
		if turn%2 == 0:
			loc = int(input('Player 1: Enter a Location: '));
			loc = loc-1
			while(board[loc] != '-'):
				loc = int(input('Enter a LEGAL location '));
				loc = loc-1
			board = insertX(board, loc)
		else:
			print(database[board])
			loc = weightedProb(database[board])
			board = insertO(board, loc)
		turn = turn + 1
	printBoard(board)
	print(gameSet)
	if isWin(board) == False:
		print("Game has ended in a tie")
	elif isWin(board) == 'X':
		print("Player Wins")
	elif isWin(board) == 'O':
		print ("Computer Wins")
main()


