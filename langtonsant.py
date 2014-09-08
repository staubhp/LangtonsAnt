import pygame
import time
import sys
import random


#start variables
gridSize =128 
pauseTime = 0.0
windowWidth = 640
windowHeight =640 
screen = pygame.display.set_mode((windowWidth,windowHeight))
running = 1
squareSize = 4
margin = 1 
backgroundColor = (214, 214, 214)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

class Ant(object):
	location =(int(gridSize/2), int(gridSize/2)) 
	cardinal = "N"
#end variables

#start functions
def initGrid(gridSize):
	grid = [[random.randrange(0,1) for i in range(gridSize)] for i in range(gridSize)]
	return grid;

def drawGrid(grid):
	for i in range(gridSize):
		for j in range(gridSize):
		    xCoord = (i*(squareSize+ margin))
		    yCoord = (j*(squareSize+margin))
		    
		    if grid[i][j] == 1:
			    color = white
		    else:
			    color = black
		    if ((i,j) == ant.location):
			    color = red
		    
		    pygame.draw.rect(screen, color, (xCoord, yCoord, squareSize, squareSize))
	pygame.display.flip()
	return;

def langton(ant):
	antX = ant.location[0]
	antY = ant.location[1]
	currentSquare = grid[antX][antY]
	direction = "right"
	if (currentSquare == 0):
		direction ="left"
	print("Ant is at ("+ str(antX) + ", " +str(antY)+") and turning " + direction) 
	if (currentSquare == 1): #black square, turn left
		grid[antX][antY] = 0
	else:#white square, turn right
		grid[antX][antY] = 1
	ant = moveAnt(ant, direction)
	drawGrid(grid)
	time.sleep(pauseTime)
	return ant;

def moveAnt(ant, direction):
	antX = ant.location[0]
	antY = ant.location[1]
	#first turn the ant 
	if (direction == "left"):
		if (ant.cardinal =="N"):
			ant.cardinal = "W"
		elif (ant.cardinal =="E"):
			ant.cardinal = "N"
		elif (ant.cardinal == "S"):
			ant.cardinal = "E"
		elif (ant.cardinal == "W"):
			ant.cardinal = "S"
	else:
		if (ant.cardinal == "N"):
			ant.cardinal = "E"
		elif (ant.cardinal =="E"):
			ant.cardinal = "S"
		elif (ant.cardinal == "S"):
			ant.cardinal = "W"
		elif (ant.cardinal == "W"):
			ant.cardinal = "N"

        #now move it forward a space
	if (ant.cardinal == "N"):
		antY = antY-1
	elif (ant.cardinal == "E"):
		antX = antX +1
	elif (ant.cardinal =="S"):
		antY = antY+1
	elif (ant.cardinal =="W"):
		antX = antX -1 
	
	ant.location = (antX, antY)
	return ant;

#end functions

#start init
ant = Ant()
screen.fill(backgroundColor)
grid = initGrid(gridSize)
drawGrid(grid)
#end init

#start loop
while running:
	event = pygame.event.poll()
	ant = langton(ant)
	if event.type == pygame.QUIT:
		running = 0
#end loop
