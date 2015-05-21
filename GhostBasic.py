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

   def insert(self, stng):
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
      if len(stng) == 0:
         List = []
         for key in self.children:
            List.append(key)
         return str(random.choice(List))
      return self.children[stng[0]].searchForNextLetter(stng[1:])

def printGhostDirections():
   print(' +-------------------------------+')
   print(' | Welcome to the game of GHOST  |')
   print(' | The human goes first. Enter   |')
   print(' | your letters in the pop-up    |')
   print(' | dialog boxes. Good luck.      |')
   print(' +-------------------------------+')

def createTrieFromDictionaryFile(root):
   file1 = open('ghostDictionary.txt')
   for word in file1:
      root.insert(word.lower().strip())
   file1.close()
   return root

# def spellWordfromString(root, stng):
#                

def requestandCheckHumanMove(root, stng):
   stng += input('HUMAN, enter your character: ').lower()[0]
   print(' ', stng)
   if root.search(stng) == True:
      if len(stng) > 3:
         print('----------------------------------------')
         print(' HUMAN LOSES because "', stng, '" is a word.', sep = '')
         print('--------------< GAME OVER >-------------')
         exit()
   if root.fragmentInDictionary(stng) == False:
      print('----------------------------------------')
      print(' HUMAN LOSES because"', stng, \
            '"\n does not begin any word.', sep = '')
      # print(" [The computer's word was ", '"', \
#               spellWordfromString(root, stng[0:-1]), '".]', sep = '')
      print('--------------< GAME OVER >-------------')
      exit()
   return(stng)

def requestandCheckComputerMove(root, stng):
   stng += root.searchForNextLetter(stng)
   print(' ', stng)
   if root.search(stng) == True:
      if len(stng) > 3:
         print('----------------------------------------')
         print(' COMPUTER LOSES because "', stng, '" is a word.', sep = '')
         print('--------------< GAME OVER >-------------')
         exit()
   if root.fragmentInDictionary(stng) == False:
      print('----------------------------------------')
      print(' COMPUTER LOSES because"', stng, \
            '"\n does not begin any word.', sep = '')
      # print(" [The human's word was ", '"', \
#               spellWordfromString(root, stng[0:-1]), '".]', sep = '')
      print('--------------< GAME OVER >-------------')
      exit()
   return(stng)

def spellWordFromString(root, stng):
  print('len string ;', len(stng))
  while stng[len(stng) - 1] != '$':
    print('stng is ', stng)
    stng += root.searchForNextLetter(stng)
  return stng[:-1]
   
def main():
   root = Node('*')
   root = createTrieFromDictionaryFile(root)
   printGhostDirections()
   stng = ''
   while True:
      stng = requestandCheckHumanMove(root, stng)
      stng = requestandCheckComputerMove(root, stng)
      
if __name__ == '__main__':
   main()
