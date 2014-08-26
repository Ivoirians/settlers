class Gaia :
	id = 0



class Board(object) :
	def __init__(self):
		print("what what")

	def createHexagon(self, lengthA = 3, lengthB = 3, lengthC = 3) :
		numTiles = lengthA * lengthB * lengthC - (lengthA - 1) * (lengthB - 1) * (lengthC - 1)
		print numTiles
		self.tiles = [0] * numTiles
		a = min(lengthA, lengthB, lengthC)
		c = max(lengthA, lengthB, lengthC)
		b = lengthA + lengthB + lengthC - a - c
		maxRow = a + b - 1
		reps = c - b + 1
		hexCounter = 0
		for hexagon in range(a) :
			newTile = Tile(hexCounter)
			self.tiles[hexCounter] = newTile

			hexCounter+=1
		for row in range(1, b):
			for hexagon in range(a + row) :
				self.tiles[hexCounter] = Tile(hexCounter)
				hexCounter+=1
		for row in range(1, c - a - b) :
			for hexagon in range(a + b - 1) :
				self.tiles[hexCounter] = Tile(hexCounter)
				hexCounter+=1
		for row in range(0, b) :
			for hexagon in range(a + b - row) :
				self.tiles[hexCounter] = Tile(hexCounter)
				hexCounter+=1
		return self.tiles

class Tile(object) :
	# Clockwise from due north: 0, 1, 2, 3, 4, 5
	def __init__(self, tileId):
		self.settlements = [0] * 6
		self.tileId = chr(tileId + 65)
		print self.tileId
		for index in range(6) :
			self.settlements[index] = str(self.tileId) + str(index)

	def __str__(self) :
		return str(self.tileId) + " " + str(self.settlements)

	def __repr__(self) :
		return self.__str__()
	def link(self, tileB, direction):
		return


class Road (object):

	def __init__(self):
		print ("New Road")


class Settlement (object) :
	owner = "Gaia"
	city = False

	def __init__(self):
		print ("New Settlement.")


def main():
	b = Board()
	t = Tile(5)
	print(t)
	print range(1, 0)
	#print(Tile(10))
	#print b.createHexagon(3, 3, 3)


main()

