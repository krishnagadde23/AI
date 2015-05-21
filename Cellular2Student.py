def setUpCanvas(root):
	root.title("Wolfram's cellular automata")
	canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def printList(rule):
	canvas.create_text(170, 20, text = 'Rule ' + str(rule), fill = 'gold', font = ('Helvetica', 10, 'bold'))
	L = [1]
	canvas.create_text(650, 10, text = chr(9607), fill = 'RED', font = ('Helvetica', FSIZE, 'bold'))
	for row in range(1, 40):
		L = [0,0] + L + [0,0]

from tkinter import Tk, Canvas, BOTH, YES
from time import clock
root = Tk()
canvas = setUpCanvas(root)
FSIZE = 2

def main():
	rule = [1,1,1,1,1,1,1,1]
	printList(rule)
	root.mainloop()

main()
