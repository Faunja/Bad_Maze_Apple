import pygame, time
from pygame.locals import *
from pygame import mixer

class define_User:
	def __init__(self):
		pygame.init()
		mixer.init()
		mixer.music.load("bad_apple.wav")
		mixer.music.set_volume(1)
		mixer.music.play()
		Display = pygame.display.get_desktop_sizes()
		self.ScreenWidth = Display[0][0]
		self.ScreenHeight = Display[0][1]

		self.FPS = 30
		self.clock = pygame.time.Clock()
		self.playing = True

User = define_User()

