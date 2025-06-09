import os
from PIL import Image

directory = "bad_apple_images/"
images = sorted(os.listdir(directory))

for renamed in images:
	split = "apple_"
	first, second = renamed.split(split)
	if len(second) == 7:
		second = "0"+second
	os.rename(directory+renamed, directory+first+split+second)
