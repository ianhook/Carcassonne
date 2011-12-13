from tileimage import TileImage
from tile import Tile
from currenttile import CurrentTile
import random

class TileFactory():
	
	baseImage = TileImage('test_tiles.png')
	count = 0
	size = (126,126)

	def newTile(self, layout):
		newImage = self.baseImage.get_region(random.randint(0,3))
		newTile = Tile(newImage)
		self.count += 1
		return newTile
