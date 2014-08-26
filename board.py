import player

class Gaia :
	id = 0

class Board :
	tiles = []
	def __init__(self):
		print("what what")

class Tile :
	# Clockwise from due north: 0, 1, 2, 3, 4, 5

	def __init__(self):
		print("New Tile.")

class Road :

	def __init__(self):
		print ("New Road")


class Settlement :
	owner = Gaia()
	city = False

	def __init__(self):
		print ("New Settlement.")


def main():
	b = Board()


main()

