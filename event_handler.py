import pygame
from pygame.locals import *
from User.define_user import User
from define_bad_apple import Bad_Apple
from User.define_controls import Controls
from Display.define_display import Display

def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == Controls.quitGame:
				User.playing = False

			if event.key in Controls.fullscreen:
				Display.toggle_fullscreen()

		if event.type == pygame.VIDEORESIZE:
			width, height = event.size
			Display.change_displaySize(width, height)
		if event.type == pygame.QUIT:
			User.playing = False
		
	Bad_Apple.play()

