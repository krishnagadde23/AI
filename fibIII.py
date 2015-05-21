
from time import clock
from math import sqrt
def main():
	n = 80; start = clock()
	print('1. fib5(',n,') = ', fib7(n))
	print('Time = ', round(clock() - start, 1), 'seconds')

def fib1(num):
	a = 0
	b = 1
	for x in range(num):
		c = a
		a = b
		b = c
	return b

def fib2(num):
	if num < 3:
		return 1
	else:
		return fib2(num - 1) + fib2(num - 2)

def fib3(num):
	a = 0
	b = 1
	for x in range(num):
		a, b = b, a + b
	return a

def fib4(n):
	lookup = {0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89,12:144}
	if n == 0:
		return 0
	elif 0 < n <= 2:
		return 1
	elif n in lookup and (n - 1) in lookup and (n - 2) in lookup:
		return lookup[n - 1] + lookup[n - 2]
	return fib4(n - 1) + fib4(n - 1)

def fib5(n):
	return {0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,11:89,12:144}[n]

def fib6(n):
	dic = {1:1,2:1}
	if len(dic) == n:
		return dic[n]
	return fib6

def fib7(n):
	phi1 = ((1 + sqrt(5)) / 2)
	phi2 = ((1 - sqrt(5)) / 2)
	x = (phi1**n - phi2**n) / sqrt(5)
	return x
main()

