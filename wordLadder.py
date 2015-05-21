#
# Krishna Gadde 9/2/14
from pickle import dump
#
def isNghbr( word1, word2):
   j = 0
   for x in range(0,6):
   	if (word1[x] == word2[x]):
   		j += 1
   if j == 5:
	   return True
   return False
#--------------------------------------------
def main():
	wordlist = open("words.txt").read().split()
	n = len( wordlist )
	#wordOne = input( "What Word: " )
	#for x in range(0,n):
	#	if isNghbr( wordOne, wordlist[x] ):
	#		print( wordlist[x] )

	nhbrs = {}
	x = 0
	while(x < n):
		nhbrs[wordlist[x]] = []
		for y in wordlist:
			if isNghbr( y, wordlist[x] ):
				nhbrs[wordlist[x]].append(y)
		x += 1
	print( nhbrs )

	fout = open("isNbhrs.pkl", "wb")
	dump(nhbrs, fout, protocol = 2)
	fout.close()
	print(nhbrs)

if __name__ == '__main__':
	main()



