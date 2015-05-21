from tkinter import *
from random import choice

master = Tk()
w, h = 500,500
canvas= Canvas(master, width=w, height=h)
canvas.pack()
FSIZE = 2

for r in range(0,256,10):
	r = bin(r)
	r = r[2:]
	rule = []
	for z in range(len(r),8):
		rule.append(0)
	r = list(r)
	rule = rule + r
	print(rule)
	rule = [0,0,0,1,1,1,1,0]

	L = [1,]
	for row in range(100):
		L = [0,0] + L + [0,0]
		"""
		print("L : ", end="")
		for k in L:
			print(k, end="")
		print()
		"""
		for n in range(len(L)):
			half = w/2
			if L[n] == 0:
				canvas.create_text(half - row*FSIZE + FSIZE*n,row*FSIZE+10,text = chr(9607), fill = "black", font = ('Helvetica',FSIZE,'bold'))
			if L[n] == 1:
				canvas.create_text(half - row*FSIZE + FSIZE*n,row*FSIZE+10,text = chr(9607), fill = "red", font = ('Helvetica',FSIZE,'bold'))
		canvas.update()
		newL = []
		for i in range(len(L)-2):
			b = str(L[i]) + str(L[i+1]) + str(L[i+2])
			#print(b)
			index = int(b, 2)
			#print(index)
			rrule = rule[::-1]
			newL.append(rrule[index])
		L = newL



#w.create_rectangle(x0, y0, , , fill="red")
mainloop()
