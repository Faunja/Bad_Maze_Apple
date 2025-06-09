import pygame
from pygame.locals import *
from User.define_user import User
from define_bad_apple import Bad_Apple
from Display.define_display import Display

def print_text(text, position, color = (255, 255, 255)):
	printed = Display.font.render(text, True, color)
	printed_width, printed_height = printed.get_size()
	User.Display.blit(printed, (position[0] * printed_width, position[1] * printed_height))

def display_box(Maze, boxPosition, position, number):
	box = Maze.maze[boxPosition[1]][boxPosition[0]]
	if box[0] and box[1] and box[2] and box[3]:
		return
	drawBox = [True, False, True, False]
	if boxPosition[1] != Maze.height - 1:
		if Maze.numbers[boxPosition[1] + 1][boxPosition[0]] > Maze.numbers[boxPosition[1]][boxPosition[0]]:
			drawBox[0] = False
	if boxPosition[1] == 0:
		drawBox[1] = True
	elif Maze.numbers[boxPosition[1] - 1][boxPosition[0]] < Maze.numbers[boxPosition[1]][boxPosition[0]]:
		drawBox[1] = True
	if boxPosition[0] != 0:
		if Maze.numbers[boxPosition[1]][boxPosition[0] - 1] > Maze.numbers[boxPosition[1]][boxPosition[0]]:
			drawBox[2] = False
	if boxPosition[0] == Maze.width - 1:
		drawBox[3] = True
	elif Maze.numbers[boxPosition[1]][boxPosition[0] + 1] < Maze.numbers[boxPosition[1]][boxPosition[0]]:
		drawBox[3] = True

	wallColor = (24 + number * 231, 24 + number * 231, 24 + number * 231)
	wallWidth = int(Display.tileSize / 4)
	if wallWidth < 1:
		wallWidth = 1
	if box[0] == 1 and drawBox[0]:
		pygame.draw.line(User.Display, wallColor, (position[0], position[1] + Display.tileSize), (position[0] + Display.tileSize, position[1] + Display.tileSize), wallWidth)
	if box[1] == 1 and drawBox[1]:
		pygame.draw.line(User.Display, wallColor, (position[0], position[1]), (position[0] + Display.tileSize, position[1]), wallWidth)
	if box[2] == 1 and drawBox[2]:
		pygame.draw.line(User.Display, wallColor, (position[0], position[1]), (position[0], position[1] + Display.tileSize), wallWidth)
	if box[3] == 1 and drawBox[3]:
		pygame.draw.line(User.Display, wallColor, (position[0] + Display.tileSize, position[1]), (position[0] + Display.tileSize, position[1] + Display.tileSize), wallWidth)

def draw_maze(Maze):
	if Maze == None:
		return
	for col in range(Maze.height):
		yOffset = col * Display.tileSize + Display.tileSize + Display.DisplayOffset[1]
		if yOffset < -Display.tileSize or yOffset > Display.DisplayHeight + Display.tileSize:
			continue
		for row in range(Maze.width):
			xOffset = row * Display.tileSize + Display.tileSize + Display.DisplayOffset[0]
			if xOffset < -Display.tileSize or xOffset > Display.DisplayWidth + Display.tileSize:
				continue
			display_box(Maze, [row, col], [xOffset, yOffset], Maze.numbers[col][row])

def display_game():
	pygame.draw.rect(User.Display, (0, 0, 0), (0, 0, Display.DisplayWidth, Display.DisplayHeight))
	draw_maze(Bad_Apple.Maze)
	
	
