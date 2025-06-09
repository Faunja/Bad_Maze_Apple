import pygame

class define_Controls:
	def __init__(self):
		self.quitGame = pygame.K_ESCAPE
		self.fullscreen = [pygame.K_F11]

Controls = define_Controls()
