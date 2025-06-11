import pygame, os, pickle
from pygame.locals import *
from pygame import mixer
from define_bad_apple import Bad_Apple
from User.define_user import User
from Display.display_game import display_game
from event_handler import event_handler

def main():
	mixer.music.play()
	while User.playing:
		print(User.clock.get_fps())
		User.clock.tick(User.FPS)
		event_handler()
		display_game()
		pygame.display.update()
	pygame.quit()

main()

