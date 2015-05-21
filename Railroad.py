#############################################
#     Name: Krishna Gadde                   #
#     Period: 1                             #
#     Date: 9/16/14                         #
#                                           #
#     Description:                          #
#     Uses the A* Algorithm to find the     #
#     path with the least distance in       #
#     in a railroad system                  #
#############################################
import pickle
from math import pi , acos , sin , cos
def readFromFile(filename):
   file = open(filename, 'rb')
   new_Dictionary = pickle.load(file)
   return new_Dictionary

def calcd(y1,x1, y2,x2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   
def createPositionDictionary(infilename):
   file = open(infilename, 'rb')
   pos_dict = {}
   for word in file:
      wordlist = str(word).split(' ')
      pos_dict[wordlist[0].strip('b\'')] = [wordlist[1], wordlist[2].strip('\\n\'')]           
   return pos_dict      

def createNeighborDictionary(infilename):
   file = open(infilename, 'rb')
   neigh_dict = {}
   for word in file:
      wordlist = str(word).split(' ')
      keylist = neigh_dict.keys()   
      keya = wordlist[0].strip('b\'')
      keyb = wordlist[1].strip('\\n\'') 
      if not keya in keylist:
         neigh_dict[keya] = [keyb] 
      else:
         neigh_dict[keya]= neigh_dict.get(keya) + [keyb]
      keya = wordlist[1].strip('\\n\'')
      keyb = wordlist[0].strip('b\'') 
      if not keya in keylist:
         neigh_dict[keya] = [keyb] 
      else:
         neigh_dict[keya]= neigh_dict.get(keya) + [keyb]
   return neigh_dict
   
def isInDictionary(word, dict):
   isIn = False
   keys = dict.keys()
   if word in keys:
      isIn = True
   return isIn

def getGValue(node, target, posDict):
   finG = 0
   pos1 = posDict[node]
   pos2 = posDict[target]
   finG = calcd(pos1[0], pos1[1], pos2[0], pos2[1])
   return finG
   
def getGValueNew(path, posDict):
   finG = 0
   if len(path) == 0 or len(path) == 1:
      finG = 0
   else:
      for i in range(len(path)-1):
         pos1 = posDict[str(path[i])]
         pos2 = posDict[path[i+1]]
         finG += calcd(pos1[0], pos1[1], pos2[0], pos2[1])
   return finG               
          
def countDifferences(word1, word2, posdict):
   return 0     
   
def AStar(start, end, posdict, neighdict):
   root = start
   target = end
   CLOSED = {}
   pops = 0
   path = []
   node = start
   gValue = getGValue(node, target, posdict)
   fValue = gValue + countDifferences(node, target, posdict)
   queue = [[fValue, node, path, gValue]]   
   while queue:
      if node == target:
         print("Length is " + str(len(path)+1))
         print("Pops = " + str(pops))
         print("Path is: ")
         finPath = path + [target]    
         return finPath
         break          
      queue.sort()
      (fValue, node, path, gValue) = queue.pop(0)
      pops += 1
      CLOSED[node] = gValue
      for child in neighdict[node]:
         pathNew = path + [node]
         nodeNew = child
         gValueNew = getGValue(nodeNew, target, posdict)         
         fValueNew = gValueNew + countDifferences(nodeNew, target, posdict)
         newChild = (fValueNew, nodeNew, pathNew, gValueNew)
         if nodeNew in CLOSED:
            oldGValue = CLOSED[nodeNew]
            if oldGValue > gValueNew:
               del CLOSED[nodeNew]
               CLOSED[nodeNew] = gValueNew
               queue.append(newChild)
         else:
            pos = -10
            for index in range(len(queue)):
               if queue[index][1] == newChild[1]:
                  pos = index
            if pos == -10:
               queue.append(newChild)
            else:   
               oldgValue = queue[pos][3]
               if oldgValue > gValueNew:
                  queue.remove(queue[pos]) 
                  queue.append(newChild)   
                     
   if node != end:
      print("Not possible")
      

sword = input("Enter starting place (enter exit to quit): ")
eword = input("Enter ending place (enter exit to quit):   ")
PosDict = createPositionDictionary("rrNodes.txt")
NeDict = createNeighborDictionary("rrEdges.txt")
if sword != "exit" and eword != "exit":
   if isInDictionary(sword, PosDict) and isInDictionary(eword, PosDict):
      finPath = AStar(sword, eword, PosDict, NeDict)
      print(finPath)
      print("Distance = " + str(getGValueNew(finPath, PosDict)))
   else:
      print("One or more values do not exist. Exiting Program...")
else:
   print("Exiting Program...")
