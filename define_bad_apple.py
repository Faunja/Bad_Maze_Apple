import os, pickle, copy, time
from PIL import Image
from define_maze import define_Maze
from User.define_user import User

class define_Bad_Apple:
	def __init__(self):
		self.imageDirectory = "bad_apple_images/"
		self.mazeDirectory = "bad_apple_mazes/"
		self.images = sorted(os.listdir(self.imageDirectory))
		self.sequence = 0
		self.referenceChange = 3
		self.clusterSize = 20
		self.play()

	def play(self):
		imagePath = self.imageDirectory+self.images[self.sequence]
		fileName = self.mazeDirectory+imagePath.split("/")[-1].split(".")[0]+".pkl"
		if os.path.exists(fileName):
			with open(fileName, 'rb') as file:
				self.Maze = pickle.load(file)
		else:
			imageFile = Image.open(imagePath).convert('RGB')
			pixelColors = imageFile.load()
			width, height = imageFile.size
			mazeWidth = int(width / self.clusterSize)
			mazeHeight = int(height / self.clusterSize)
			if not self.sequence % self.referenceChange:
				self.referenceMaze = define_Maze(mazeWidth, mazeHeight)
			self.Maze = define_Maze(2, 2)
			currentVariables = vars(self.Maze)
			referenceVariables = vars(self.referenceMaze)
			for variable in currentVariables:
				if variable in referenceVariables:
					if isinstance(referenceVariables[variable], list):
						currentVariables[variable] = copy.deepcopy(referenceVariables[variable])
					else:
						currentVariables[variable] = referenceVariables[variable]
			for mazeY in range(mazeHeight):
				clusteryPosition = mazeY * self.clusterSize
				for mazeX in range(mazeWidth):
					clusterxPosition = mazeX * self.clusterSize
					colorValue = [0, 0]
					for y in range(self.clusterSize):
						yPosition = y + clusteryPosition
						for x in range(self.clusterSize):
							xPosition = x + clusterxPosition
							r, g, b = pixelColors[xPosition, yPosition]
							colorValue[round((r + g + b) / 3 / 255)] += 1
					if colorValue[0] > colorValue[1]:
						self.Maze.numbers[mazeY][mazeX] = 0
					else:
						self.Maze.numbers[mazeY][mazeX] = 1
			with open(fileName, 'wb') as file:
				pickle.dump(self.Maze, file)
			with open("Bad_Apple.pkl", 'wb') as file:
				pickle.dump(self, file)
		self.sequence += 1
		if self.sequence == len(self.images) - 1:
			User.playing = False

Bad_Apple = define_Bad_Apple()
if os.path.exists("Bad_Apple.pkl"):
	with open("Bad_Apple.pkl", "rb") as file:
		Old_Apple = pickle.load(file)
		if Bad_Apple.clusterSize == Old_Apple.clusterSize:
			Bad_Apple.referenceMaze = Old_Apple.referenceMaze


