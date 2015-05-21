def setUpCanvas(root): # These are the REQUIRED magic lines to enter graphics mode.
	root.title("THE AUTOMATIC ANT by (Tanvir). ")
	canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def placeFrameAroundWindow():
	canvas.create_rectangle(5, 5, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, outline = 'GOLD')

def displayStatistics(startTime):
	elapsedTime      = round(clock() - startTime, 2)
	sppedPerThousand  = round(1000*elapsedTime/STEPS, 2)
	print('+=======< Automated Ant Statistics>=======+')
	print('| ANT MOVES = ', STEPS, 'steps.               |')
	print('| RUN TIME =%6.2f'%elapsedTime,        'seconds.                |')
	print('| SPEED    =%6.2f' % sppedPerThousand, 'seconds-per-1000-moves. |') 
	print('+===========================================+')
	message = 'PROGRAM DONE. Final image is ' + str(STEPS) + 'ant moves in ' + str(elapsedTime) + 'seconds.'
	root.title(message)

def displayMatrix(matrix): #used for debugging
	print('---MATRIX:')
	for row in matrix:
		[print (x, ' ', end = '') for x in row]
		print()
	print(' =======================')

def plot(x, y, kolor = 'WHITE'): #Plots 5x5 "points" on video screen
	canvas.create_rectangle(x, y, x+5, y+5, width = 1, fill = kolor)

def createPixelWorld():
#---Size matrix (the pixel word)
	ROW = SCREEN_HEIGHT + 5
	COL = SCREEN_WIDTH  + 5

#---Fill world with cells all the same color: WHITE (0). Note matrix[row][col]
	matrix = [[0 for c in range(COL)]
					for r in range(ROW)]

#---place ant in pixel world (ant[0] = 0 means ant moves up.)
	placeFrameAroundWindow()
	canvas.create_line(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, fill = 'RED')
	ant = [0, ANT_START_ROW, ANT_START_COL]
	return ant, matrix

def move(ant): # ant = [direction(0), col(1), row(2)]
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

def modifyColors(ant, matrix):
#---Get color of new cell.
	color = matrix[ant[2]][ant[1]] 
	if color == 0 or color == 3:  
	  ant = [(ant[0]+1)%4, ant[1], ant[2]]
	elif color == 1 or color == 2:  
	  ant = [ant[0] - 1, ant[1], ant[2]]
	if ant[0] == -1:
	  ant = [3, ant[1], ant[2]]
	#---Find number of next color. 
	newcolor = color + 1
	if newcolor > 3:
	  newcolor = 0
	#---Flip the new cell's color in matrix.
	matrix[ant[2]][ant[1]] = newcolor
	#---Display the new cell's color on screen. 
	plot(ant[1], ant[2], COLORS[newcolor])
	return ant

def makeTheAntsJourney(ant, matrix):
	message = 'PROGRAM CURRENTLY RUNNING ' + str(STEPS) + ' ant moves in ' + str(SPEED_INC) + ' increments.'
	print(message)
	root.title(message)
	startTime = clock()
	for n in range (STEPS):
		ant = move(ant)
		ant = modifyColors(ant, matrix)
		if n % SPEED_INC == 0:
			canvas.update()
	canvas.update()
	displayStatistics(startTime)

from tkinter import Tk, Canvas, YES, BOTH
from time 	 import clock
from random  import choice
root             = Tk()
canvas           = setUpCanvas(root)
#--Below the numbers have been chosen to all be divisible by 5, since each "point" is a 5x5 pixel square. 
SCREEN_WIDTH     = root.winfo_screenwidth() //5*5 - 15 # adjusted to exclude task bars on my PC. 
SCREEN_HEIGHT    = root.winfo_screenheight()//5*5 - 90 # adjusted to exclude task bars on my PC. 
ANT_START_ROW    = SCREEN_WIDTH //(5*2) * 5
ANT_START_COL    = SCREEN_HEIGHT//(5*2) * 5
STEPS            = 20000
SPEED_INC        = 20
COLORS           = ('WHITE', 'RED', 'BLUE', 'YELLOW', 'GREEN', 'CYAN', 'MAGENTA', 'GRAY', 'PINK')
HEADING_RULE     = (0,1)
#HEADING_RULE    = (0,1,1,0) # also (0,0,1,1,0,0). Are there others? This may be useful in Part II
assert len(HEADING_RULE) < len(COLORS)
NUMBER_OF_COLORS = len(HEADING_RULE)

def main(): 
	ant, matrix = createPixelWorld()
	makeTheAntsJourney(ant, matrix)
	root.mainloop() # Required for graphics. 

main()