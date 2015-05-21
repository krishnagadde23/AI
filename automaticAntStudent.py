def setUpCanvas(root):
	root.title("THE AUTOMATIC ANT BY KRISHNA GADDE.")
	canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def placeFrameAroundWindow():
	canvas.create_rectangle(5, 5, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, outline = 'GOLD')
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def displayStatistics(startTime):
	elapsedTime 	  = round(clock() - startTime, 2)
	speedPerThousand  = round(1000*elapsedTime/STEPS, 2)
	print('+=======< AUTOMATED ANT STATISTICS >========+')
	print('| ANT MOVES = ', STEPS, 'steps.  				|')
	print('| RUN TIME  =%6.2f'% elapsedTime, 		'seconds.				   |')
	print('| SPEED     =%6.2f' % speedPerThousand, 	'seconds-per-1000-moves.   |')
	print('+============================================+')
	message = 'PROGRAM DONE. Final image is ' +str(STEPS)+ ' ant moves in ' + str(elapsedTime) + ' seconds.'
	root.title(message)
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def displayMatrix(matrix):
	print('---MATRIX:')
	for row in matrix:
		[print (x, ' ', end = '') for x in row]
		print()
	print ('	==============================')
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def plot(x, y, kolor = 'WHITE'):
	canvas.create_rectangle(x, y, x+5, y+5, width = 1, fill = kolor)
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def createPixelWorld():
#---Size matrix (the pixel world)
	ROW = SCREEN_HEIGHT + 5
	COL = SCREEN_WIDTH + 5

#---Fill world with cells all the same color: WHITE (0). Note matrix[row][col]
	matrix = [[0 for c in range(COL)] for c in range(ROW)]

#---place ant in pixel world (ant[0] = 0 means ant moves up.)
	placeFrameAroundWindow()
	canvas.create_line(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, fill = 'RED')
	ant = [0, ANT_START_ROW, ANT_START_COL]
	return ant, matrix
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def move(ant):
#---move ant forward to next cell.
	if ant[0] == 0:
		ant = [ant[0], ant[1], ant[2] - 5]
	if ant[0] == 1:
		ant = [ant[0], ant[1] - 5, ant[2]]
	if ant[0] == 2:
		ant = [ant[0], ant[1], ant[2] + 5]
	if ant[0] == 3:
		ant = [ant[0], ant[1] + 5, ant[2]]

#---Wrap around, if necessary.
	if ant[1] > SCREEN_WIDTH:
		ant[1] = 5
	if ant[1] < 5:
		ant[1] = SCREEN_WIDTH

	if ant[2] > SCREEN_HEIGHT:
		ant[2] = 5
	if ant[2] < 5:
		ant[2] = SCREEN_HEIGHT

	return ant
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def modifyColors(ant, matrix):
	
#---Get color of new cell.
	color = matrix[ant[2]][ant[1]]
#---Change ant's direction depending on the color of the cell. The code below assumes 2 colors.
	if color == 0:
		ant = [(ant[0] + 1) % 4, ant[1], ant[2]]
	elif color == 1:
		ant = [(ant[1] - 1), ant[1], ant[2]]
	if ant[0] == -1:
		ant = [3, ant[1], ant[2]]
#---Find number of next color.
	newColor = color + 1
	if color > 1:
		newColor = 0
#---Flip the new cell's color in matrix.
	matrix[ant[2]][ant[1]] = newColor
#---Display the new cell's color on screen.
	plot(ant[1], ant[2], COLORS[newColor])
	return ant
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
def maketheAntsJourney(ant, matrix):
	message = 'PROGRAM CURRENTLY RUNNING ' + str(STEPS) + ' ant moves in ' + str(SPEED_INC) + ' increments.'
	print(message)
	root.title(message)
	startTime = clock()
	for n in range(STEPS):
		move(ant)
		modifyColors(ant, matrix)
		if n % SPEED_INC == 0:
			canvas.update()
	canvas.update()
	displayStatistics(startTime)
#---------------------------<GLOBAL CONSTANTS AND GLOBAL IMPORTS>----------------------------AUTOMATED ANT--
from tkinter import Tk, Canvas, YES, BOTH
from time import clock
from random import choice
root = Tk()
canvas = setUpCanvas(root)
#--Below the numbers have been chosen to all be divisible by 5, since each "point" is a 5x5 pixel square.
SCREEN_WIDTH = root.winfo_screenwidth() //5*5 - 15
SCREEN_HEIGHT = root.winfo_screenheight() //5*5 - 90
ANT_START_ROW = SCREEN_WIDTH//(5*2) * 5
ANT_START_COL = SCREEN_HEIGHT//(5*2) * 5
STEPS = 20000
SPEED_INC = 20
COLORS = ('WHITE', 'RED', 'BLUE', 'YELLOW', 'GREEN', 'CYAN', 'MAGENTA', 'GRAY', 'PINK')
HEADING_RULE = (0,1)
assert len(HEADING_RULE) < len(COLORS)
NUMBER_OF_COLORS = len(HEADING_RULE)
#--------------------------------------------------------------------------------------------AUTOMATED ANT--

def main():
	ant, matrix = createPixelWorld()
	maketheAntsJourney(ant, matrix)
	root.mainloop()
#--------------------------------------------------------------------------------------------AUTOMATED ANT--
main()
