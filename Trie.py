import string
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
   
from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock

def main():
   root = Node('*')
   root.insert('cat')
   root.insert('catnip')
   root.insert('cats')
   root.insert('catnap')
   root.insert("can't")
   root.insert('cat-x')
   root.insert('dog')
   root.insert('dogs')
   root.insert('dognip')
   root.print('')
  #  root.display()
   print('SEARCH:', root.search("c"))
   printElapsedTime()

def printElapsedTime():
   print('\n---Total run time =', round(clock() - startTime, 2), 'seconds.')
   
if __name__ == '__main__': startTime = clock(); main()
            
