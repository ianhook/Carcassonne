from kivy.uix.image import Image
from kivy.resources import resource_find
from kivy.logger import Logger

class TileImage():

	def __init__(self, source):
		self.tile_size = (126,126)
		self.texture = Image(source=source).texture

	#def _set_texture(self, value):
		#filename = resource_find(self.source)
		#self.texture = CoreImage(filename)
		#(x,y,width,height) = self.select_region()
		#self.texture = self.texture.get_region(x,y,width,height)
		#Logger.info('hi ' + str(self.texture) + ' ' + str(x) + ':' + str(y))

	def get_region(self, pos):
		num_wide = self.texture.size[0] / self.tile_size[0]
		num_high = self.texture.size[1] / self.tile_size[1]
		if num_high == 0 or num_wide == 0:
			return (0,0,1,1)
		if pos > num_wide * num_high:
			return None
			#this is an error
		else:	
			#(x,y) = (0,0)
			x = pos % num_wide * self.tile_size[0]
			y = pos / num_wide * self.tile_size[1]
			Logger.info('%d %d %d, %d %d',pos, num_wide, num_high, x, y )
			#self.texture = self.image.texture.get_region(x,y,width,height)
			r = Image(size=self.tile_size)
			r.texture = self.texture.get_region(x,y,self.tile_size[0],self.tile_size[1])
			return r
