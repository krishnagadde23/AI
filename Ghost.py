#############################################
#     Name: Krishna Gadde                   #
#     Period: 1                             #
#     Date: 12/1/14                         #
#                                           #
#     Description:                          #
#     GHOST GAME							#
#	  Game that uses the Trie class			#
#############################################
import copy
from random import choice
import string
import random

class Node(object):
   def __init__ (self, value):
      self.value = value
      self.children = {}
   def __repr__ (self):
      self.print()
      return ' '
   def print(self, stng):
      for children in self.children:
         if children == '$':
            print(stng + self.value)
         elif self.value == '*':
            self.children[children].print(stng)
         else:
            self.children[children].print(stng + self.value)
                  
   def display(self):
      if self.value == '$': return
      print('========== NODE ==========')
      print ('--> self.value = ', self.value)
      print ('--> self.children: [', end = '')
      for key in self.children:
         print(key, sep = '', end = ', ')
      print(']')
      print('--------------------------')
      
      for char in self.children:
         (self.children[char]).display()

   def insert(stng):
      if len(stng) == 0:        
         self.children['$'] = Node('$')
      elif stng[0] in self.children:
         self.children[stng[0]].insert(stng[1:])
      elif not stng[0].isalpha():
         stng = stng[1:]
         p = Node(stng[0])
         self.children[p.value] = p
         p.insert(stng[1:])
      elif stng[0] not in self.children:
         p = Node(stng[0])
         self.children[p.value] = p
         p.insert(stng[1:])               
         
   def search(self, stng):                  
      if len(stng) == 0:
         if '$' in self.children:
            return True     
      else:
         for c in string.punctuation:
            stng = stng.replace(c, '')
         if stng[0] in self.children:                                   
            return self.children[stng[0]].search(stng[1:])
      return False
   
   def fragmentInDictionary(self, stng):
      if len(stng) == 0:
         return True           
      else:
         for c in string.punctuation:
            stng = stng.replace(c, '')
         if stng[0] in self.children:                                   
            return self.children[stng[0]].fragmentInDictionary(stng[1:])
         return False
   
   def display(self):
      if self.value == '$': return
      print('========== NODE ==========')
      print ('--> self.value = ', self.value)
      print ('--> self.children: [', end = '')
      for key in self.children:
         print(key, sep = '', end = ', ')
      print(']')
      print('--------------------------')
      
      for char in self.children:
         (self.children[char]).display()
   
   def searchForNextLetter(self, stng):      
      if len(stng) == 1:
         list = []
         for key in self.children:
            list.append(key)
         return random.choice(list)
      self.children[stng[0]].searchForNextLetter(stng[1:])

def recursivelyReturnLetter(string, player, N, dictionary, cur):
	if string in dictionary:
		if player == cur:
			return 1
		else:
			return 0
	poss = []
	for word in dictionary:
		if word[:len(string)] == string:
			if word[len(string)] not in poss:
				poss.append(word[len(string)])
	if len(poss) == 0:
		if player == cur:
			return 1
		else:
			return 0
	prob = 0
	for letter in poss:
		prob += recursivelyReturnLetter(string+letter, (player + 1) % 2, 2, dictionary, cur)
	return prob/len(poss)

def getHintFromTrie(string, player, dictionary):
	if string in dictionary:
		return ["CHALLENGE"]
	poss = []
	temp = copy.deepcopy(dictionary)
	for word in dictionary:
		if word[:len(string)] == string:
			if word[len(string)] not in poss:
				poss.append(word[len(string)])
		else:
			temp.remove(word)
	dictionary = temp
	print("Possible Choices: " + str(poss))
	if len(poss) == 0:
		return ["CHALLENGE"]
	ch = []
	prob = 0.0
	for letter in poss:
		trial = recursivelyReturnLetter(string + letter, (player + 1) % 2, 2, dictionary, player)
		if trial > prob:
			prob = trial
			ch = [letter]
		elif trial == prob:
			ch.append(letter)
	return ch

def printGhostDirections():
	print("*------------------------------*")
	print("| Welcome to the game of GHOST |")
	print("| Player 1 goes first. Enter   |")
	print("| your letters in the dialog   |")
	print("| boxes. Good Luck.            |")
	print("*------------------------------*")

def createTrieFromDictionaryFile():
   root = []
   file1 = open('ghostDictionary.txt')
   for word in file1:
      root.append(word.lower().strip())
   file1.close()
   return root

def ghostGame(root):
	N = int(input("How many players? "))
	players = []
	for i in range (0, N):
		players.append("")
	while 1:
		dic = copy.deepcopy(root)
		cur = 0
		word = ""
		while 1:
			if players[cur] != "GHOST":
				print("Player " + str(cur + 1) + "'s turn")
			else:
				cur = (cur + 1) % N
				continue
			print("Current String: " + word)
			inp = input("What letter do you choose? ")
			if inp == "quit":
				print("Player " + str(cur + 1) + " has quit.")
				exit()
			if inp == "?":
				print("Best choices: " + str(getHintFromTrie(word, cur, dic)))
			if inp == "CHALLENGE":
				if word not in dic:
					players[cur - 1] += "GHOST"[len(players[cur-1])]
				if word in dic:
					print("Incorrect CHALLENGE:" + word + " is a valid word.")
					players[cur] += "GHOST"[len(players[cur])]
				if cur == 0:
					print("Player " + str(N) + " now has " + str(players[cur-1]))
				else:
					print("Player " + str(cur) + " now has " + str(players[cur-1]))
				cur = (cur + 1) % N
				break
			if inp != "?":
				word += inp
				cur = (cur + 1) % N
		print("Progress: " + str(players))
		count = 0
		for i in range(0, N):
			if players[i] == "GHOST":
				count += 1
		if count == N-1:
			print("Game Over")
def main():
	root = createTrieFromDictionaryFile()
	printGhostDirections()
	ghostGame(root)

main()
