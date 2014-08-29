class Pair(frozenset):
	#nothing actually keeps this a pair right now
	def __str__(self) :
		x = list(self)
		return "[" + str(x[0]) + "," + str(x[1]) + "]"

	def __repr__(self) :
		return self.__str__()


class Resources(object):

    DESERT = "Desert"
    BRICK = "Brick"
    WOOD = "Wood"
    SHEEP = "Sheep"
    ORE = "Ore"
    WHEAT = "Wheat"

class Board(object) :

	def __init__(self):
		self.tiles = {}
		self.settlements = {}
		self.roads = {}
		self.createBoard()

	def createBoard(self) :
		for z in range(-2, 3) :
			for x in range(max(-2, -2 - z), min(2, 2 - z) + 1):
				y = - x - z
				t = Tile(x, y, z, self)
				self.tiles[(x, y, z)] = t
				for n in t.getVertices():
					self.addSettlement(n)

		for s in self.settlements:
			for k in self.settlements[s].neighboringVertices():
				r = Road(s, k)
				self.roads[r.endpoints] = r

	def addSettlement(self, vertex) :
		self.settlements[vertex] = Settlement(vertex, self)

	def buildSettlement(self, vertex, owner) :
		if not self.validVertex(vertex):
			print "Not a valid vertex"
			return False
		newS = self.settlements[vertex]
		neighbors = newS.neighboringVertices()
		for v in neighbors:
			if self.settlements[v].owner != "Gaia":
				print "Too close to existing settlement"
				return False
		if newS.changeOwner(owner) == False:
			print "Already existing settlement"
			return False
		self.settlements[vertex] = newS
		return True

	def validVertex(self, vertex) :
		return vertex in self.settlements.keys()		

	def __str__(self) :
		return str(self.tiles) + "\n" + str(self.settlements) + "\n" + str(self.roads)

	def __repr__(self) :
		return self.__str__()

class Settlement (object) :

	def __init__(self, settlement, board):
		self.x, self.y, self.z = settlement
		self.board = board
		self.owner = "Gaia"
		self.city = False

	def neighboringVertices(self):

		if (self.x + self.y + self.z) % 2 == 0:
			neighbors = [(self.x, self.y, self.z - 1), (self.x - 1, self.y, self.z), (self.x, self.y - 1, self.z)]
		else :
			neighbors = [(self.x, self.y, self.z + 1), (self.x + 1, self.y, self.z), (self.x, self.y + 1, self.z)]
		return filter(self.board.validVertex, neighbors)

	def changeOwner(self, owner) :
		if self.owner == "Gaia":
			self.owner = owner
			return True
		else:
			return False

	def __str__(self) :
		return "[Settlement|" + str((self.x, self.y, self.z)) + "|" + str(self.owner) + "|" + str(self.city) + "]"

	def __repr__(self) :
		return self.__str__()

class Road (object) :

	def __init__(self, x, y):
		self.endpoints = Pair([x, y])
		self.owner = "Gaia"

	def changeOwner(self, owner) :
		if self.owner == "Gaia":
			self.owner = owner

	def __str__(self) :
		ends = tuple(self.endpoints)
		return "[Road|" + str(ends) + "|" + str(self.owner) + "]"

	def __repr__(self) :
		return self.__str__()

class Tile(object) :

	def __init__(self, x, y, z, board):
		self.x, self.y, self.z = x, y, z
		self.board = board
		self.resource = None

	def __str__(self) :
		return "[Tile|" + str((self.x, self.y, self.z)) + "|" + str(self.resource) + "]"

	def __repr__(self) :
		return self.__str__()

	def setResource(self, resource):
		self.resource = resource

	def getVertices(self):
		x, y, z = self.x, self.y, self.z
		return ((x, y, z), (x-1, y, z), (x, y-1, z), (x, y-1, z+1), (x-1, y, z+1), (x-1, y-1, z+1))

def tests():
	b = Board()
	assert len(b.settlements.keys()) == 54
	assert len(b.tiles.keys()) == 19
	assert len(b.roads.keys()) == 72
	print b.buildSettlement((0, 0, 0), "blue")
	print b.buildSettlement((1, 0, -1), "red")
	print b.buildSettlement((1, -1, 0), "yellow")
	print ("All tests passed")

def main():
	tests()
	b = Board()
	b.buildSettlement((1, -2, 1), False)
	b.tiles[(-1, 1, 0)].setResource(Resources.BRICK)

main()

