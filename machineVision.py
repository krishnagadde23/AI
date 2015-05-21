#############################################
#	            Krishna Gadde	        		    #
#	            Period 1			                #
#	            February 10, 2015		          #
#	            Machine Vision			          #
#############################################

from tkinter import *
from time import clock
import copy
from math import *

root = Tk()
START = clock()
COLORFLAG = False
maxR = 100
HIGH = 45
LOW = 10
WIDTH = 296
HEIGHT = 300

def main():
  image = []
  #matrix = createMatrix(dimensions, image, WIDTH, HEIGHT)
  setUpValues, grayValues = grayImage()
  blurValues = blur(setUpValues, grayValues)
  sobelValues, gValues = sobel(setUpValues, blurValues)
  #cannyVals = canny(matrix, image, WIDTH, HEIGHT, sobelValues)
  circleDetection(setUpValues, sobelValues, gValues)
  #displayImageWindow(sobelValues)
  #root.mainloop()

def printElapsedTime(msg = 'time'):
  length = 30
  msg = msg[:length]
  tab = '.'*(length-len(msg))
  print('--' + msg.upper() + tab + ' ', end = '')
  time = round(clock() - START, 1)
  print('%2d'%int(time/60), ' min:', '%4.1f'%round(time%60, 1), ' sec', sep = '')

def displayImageWindow(image):
    global x
    x = ImageFrame(image)

class ImageFrame:
  def __init__(self, image, COLORFLAG = False):
      self.img = PhotoImage(width = WIDTH, height = HEIGHT)
      for row in range(HEIGHT):
          for col in range(WIDTH):
              num = image[row*WIDTH + col]
              if COLORFLAG == True:
                  kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])
              else:
                  kolor = '#%02x%02x%02x' % (num, num, num)
              self.img.put(kolor, (col, row))
      c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
      c.create_image(0, 0, image = self.img, anchor = NW)
      printElapsedTime('displayed image')

def grayImage():
  file1 = open('circle.ppm', 'r')
  stng = file1.readline()
  dimensions = file1.readline().split()
  x = dimensions[0]
  y = dimensions[1]
  rgbValue = file1.readline()

  nums = file1.read().split()
  nums = list(map(int, nums))

  image = []
  for RGB in range(0, len(nums), 3):
    gray = int(0.3*nums[RGB] + 0.59*nums[RGB+1] + 0.11*nums[RGB+2])
    image.append(gray)
    
  outfile = open('grayCircle.ppm', 'w')
  outfile.write(stng + '\n')
  outfile.write(x + ' ' + y + '\n')
  outfile.write(rgbValue + '\n')
  
  for val in image:
    outfile.write(str(val) + ' ' + str(val) + ' ' + str(val) + ' ')
  outfile.close()

  setup = [stng, x, y, rgbValue]
  return setup, image

def blur(setUpData, grayArray):
  stng = setUpData[0]
  x = setUpData[1]
  y = setUpData[2]
  rgbVal = setUpData[3]

  blurArray = copy.deepcopy(grayArray)
  for row in range(1, HEIGHT - 1):
    for col in range(1, WIDTH - 1):
      topLeft = grayArray[(row - 1)*WIDTH + (col - 1)]
      topMiddle = grayArray[(row - 1)*WIDTH + col]
      topRight = grayArray[(row - 1)*WIDTH + (col + 1)]
      middleLeft = grayArray[row*WIDTH + (col - 1)]
      center = grayArray[row*WIDTH + col]
      middleRight = grayArray[row*WIDTH + (col + 1)]
      bottomLeft = grayArray[(row + 1)*WIDTH + (col - 1)]
      bottomMiddle = grayArray[(row + 1)*WIDTH + col]
      bottomRight = grayArray[(row + 1)*WIDTH + (col + 1)]
      blurColor = (1/16) * (topLeft + 2*topMiddle + topRight + 2*middleLeft + 4*center + 2*middleRight + bottomLeft + 2*bottomMiddle + bottomRight)
      blurArray[row*WIDTH + col] = round(blurColor)

  outfile = open('blurCircle.ppm', 'w')
  outfile.write(stng + '\n')
  outfile.write(x + ' ' + y + '\n')
  outfile.write(rgbVal + '\n')

  for val in blurArray:
    outfile.write(str(val) + ' ' + str(val) + ' ' + str(val) + ' ')
  outfile.close()

  return blurArray

def sobel(setUpData, blurArray):
  stng = setUpData[0]
  x = setUpData[1]
  y = setUpData[2]
  rgbVal = setUpData[3]

  sobelArray = copy.deepcopy(blurArray)
  gArray = [[0,0]] * WIDTH * HEIGHT

  for row in range(1, HEIGHT - 1):
    for col in range(1, WIDTH - 1):
      topLeft = blurArray[(row - 1)*WIDTH + (col - 1)]
      topMiddle = blurArray[(row - 1)*WIDTH + col]
      topRight = blurArray[(row - 1)*WIDTH + (col + 1)]
      middleLeft = blurArray[row*WIDTH + (col - 1)]
      center = blurArray[row*WIDTH + col]
      middleRight = blurArray[row*WIDTH + (col + 1)]
      bottomLeft = blurArray[(row + 1)*WIDTH + (col - 1)]
      bottomMiddle = blurArray[(row + 1)*WIDTH + col]
      bottomRight = blurArray[(row + 1)*WIDTH + (col + 1)]
      Gx = (1/8) * (-1*topLeft + topRight + -2*middleLeft + 2*middleRight + -1*bottomLeft + bottomRight)
      Gy = (1/8) * (topLeft + 2*topMiddle + topRight + -1*bottomLeft + -2*bottomMiddle + -1*bottomRight)
      gArray[row*WIDTH + col] = [Gx, Gy]
      if abs(Gx) + abs(Gy) > 60:
        sobelArray[row*WIDTH + col] = 0
      else:
        sobelArray[row*WIDTH + col] = 255

  outfile = open('sobelCircle.ppm', 'w')
  outfile.write(stng + '\n')
  outfile.write(x + ' ' + y + '\n')
  outfile.write(rgbVal + '\n')

  for val in sobelArray:
    outfile.write(str(val) + ' ' + str(val) + ' ' + str(val) + ' ')
  outfile.close()

  return sobelArray, gArray

def extractStructuredDataFromFile(fileName):
  import pickle
  fileName = open("finalData.ppm", "r")
  imageLists = pickle.load(fileName)
  fileName.close()
  return imageLists

def frange(start, stop, step):
  i = start
  while i < stop:
    yield i
    i += step

def drawCircle(image, cx, cy, radius):
  maxIndex = len(image)
  for t in frange(0, 6.28, 0.01):
    x = int(cx + radius*cos(t))
    y = int(cy + radius*sin(t))
    index = y*WIDTH + x
    if(0 <= index < maxIndex) and (0 <= x < WIDTH):
      image[index] = 254
  print('Circle Center (cx, cy) = ', cx, cy, 'radius = ', radius)
  return image

def circleDetection(setUpData, sobelArray, gValues):
  filetype = 'P3'
  x = setUpData[1]
  y = setUpData[2]
  rgbVal = setUpData[3]

  density = [0] * HEIGHT * WIDTH
  density1 = [[]] * WIDTH * HEIGHT

  for row in range(1, HEIGHT - 1):
    for col in range(1, WIDTH - 1):
      currentX = col
      currentY = row
      current = row*WIDTH + col
      Gx = gValues[current][0]
      Gy = gValues[current][1]

      if abs(Gx) + abs(Gy) > 60:
        theta = atan2(Gy, Gx)
        for R in range(350):
          cx = currentX + int(R*cos(theta))
          cy = currentY - int(R*sin(theta))
          if 0 <= cx < WIDTH and 0 <= cy < HEIGHT:
            density1[cy*WIDTH + cx].append(R)
            density[cy*WIDTH + cx] += 1

        for R in range(350):
          cx = currentX - int(R*cos(theta))
          cy = currentY + int(R*sin(theta))
          if 0 <= cx < WIDTH and 0 <= cy < HEIGHT:
            density1[cy*WIDTH + cx].append(R)
            density[cy*WIDTH + cx] += 1

  outfile = open('detectCircle.ppm', 'w')
  outfile.write(filetype + '\n')
  outfile.write(x + ' ' + y + '\n')
  outfile.write(rgbVal + '\n')

  maxVotes = 0
  maxIndex = 0

  for row in range(0, HEIGHT):
    for col in range(0, WIDTH):
      current = row*WIDTH + col
      if density[current] > maxVotes:
        maxVotes = density[current]
        maxIndex = current

  radius = sum(density1[maxIndex])//len(density1[maxIndex])
  xCenter = maxIndex%WIDTH
  yCenter = maxIndex//WIDTH
  drawCircle(density, xCenter, yCenter, radius)

  for row in range(0, HEIGHT):
    for col in range(0, WIDTH):
      current = row*WIDTH + col
      Gx = gValues[current][0]
      Gy = gValues[current][1]

      if abs(Gx) + abs(Gy) > 60:
        outfile.write(str(sobelArray[current]) + ' ' + str(sobelArray[current]) + ' ' + str(sobelArray[current]) + ' ')

      else:
        temp = density[current]
        if temp > 255:
          temp = 255
          outfile.write(str(int(255 - temp)) + ' ' + str(int(255 - temp)) + ' ' + str(int(255 - temp)) + ' ')
        elif temp == 254:
          outfile.write(str(int(0)) + ' ' + str(int(255)) + ' ' + str(int(0)) + ' ')
        else:
          outfile.write(str(int(255 - temp)) + ' ' + str(int(255 - temp)) + ' ' + str(int(255 - temp)) + ' ')


  outfile.close()

main()
