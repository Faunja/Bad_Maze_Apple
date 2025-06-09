import pygame
from pygame.locals import *
from define_bad_apple import Bad_Apple
from User.define_user import User

class define_Display:
	def __init__(self):
		self.fullscreen = True
		self.DisplayDifference = 4 / 5
		self.DisplayWidth = User.ScreenWidth
		self.DisplayHeight = User.ScreenHeight
		self.tileSize = int(self.DisplayHeight / (Bad_Apple.Maze.height + 2))
		self.DisplayOffset = [int((self.DisplayWidth - self.tileSize * Bad_Apple.Maze.width) / 2), int((self.DisplayHeight - self.tileSize * Bad_Apple.Maze.height) / 2)]
		pygame.mouse.set_visible(False)

		self.update_display(self.DisplayWidth, self.DisplayHeight, self.fullscreen)

	def update_display(self, DisplayWidth, DisplayHeight, fullscreen):
		if fullscreen == False:
			User.Display = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.RESIZABLE)
		else:
			User.Display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		if DisplayHeight < DisplayWidth:
			User.font = pygame.font.Font('Display/Fonts/m6x11.ttf', round(DisplayHeight / 32))
		else:
			User.font = pygame.font.Font('Display/Fonts/m6x11.ttf', round(DisplayWidth / 32))
		self.tileSize = int(self.DisplayHeight / (Bad_Apple.Maze.height + 2))
		self.DisplayOffset = [int((self.DisplayWidth - self.tileSize * Bad_Apple.Maze.width) / 2), int((self.DisplayHeight - self.tileSize * Bad_Apple.Maze.height) / 2)]

	def change_displaySize(self, newWidth, newHeight):
		self.DisplayWidth = newWidth
		self.DisplayHeight = newHeight
		self.update_display(self.DisplayWidth, self.DisplayHeight, self.fullscreen)
	
	def toggle_fullscreen(self):
		self.fullscreen = not self.fullscreen
		if self.fullscreen:
			self.change_displaySize(User.ScreenWidth, User.ScreenHeight)
		else:
			self.change_displaySize(round(User.ScreenWidth * self.DisplayDifference), round(User.ScreenHeight * self.DisplayDifference))

Display = define_Display()
