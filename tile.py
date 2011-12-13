class Tile():
	
	def __init__(self, image):
		self.__image = image
	
	def get_image(self):
		return self.__image

	def check_placement(self, adjects):
		'''Check to make sure that this tile can be placed next to
		the tiles in the adject dictionary.  The adject list should 
		contain keys 'north', 'south', 'east', and 'west'; their absense
		means that that space is empty.
		This function is not defined here because it is defined in the
		the TileFactory when the actual tile type is decided.
		'''
		if ('north' in adjects and adjects['north'] != self.north) or ('south' in adjects and adjects['south'] != self.south) or ('east' in adjects and adjects['east'] != self.east) or ('west' in adjects and adjects['west'] != self.west):
			return False
		return True
	
	def set_sides(self, sides):
		self.north = sides['north']
		self.south = sides['south']
		self.east = sides['east']
		self.west = sides['west']

