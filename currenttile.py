'''
Current Tile
============

This module does all of the game work.  The main program loop is created in the kivy framework behind the scenes so we only need to worry about how user input will update the screen.  For turn based games like this one it's easy enough to wait for input events and then update the screen in response.

For games with real time events a clock function will need to be used to update the screen regardless of user events. I'm not sure how this will work yet.
'''
from kivy.uix.scatter import Scatter
from kivy.properties import ListProperty
from kivy.logger import Logger

class CurrentTile(Scatter):
	
	grid = ListProperty([1, 2])

	def __init__(self, **kwargs):
		Logger.info('hi')
		kwargs.setdefault('do_scale', False)
		super(CurrentTile, self).__init__(**kwargs)
		self._set_to_grid(self.grid)

	def on_grid(self, instance, value):
		#Logger.info(value)
		self._set_to_grid(value)

	def on_touch_up(self, touch):
		super(CurrentTile, self).on_touch_up(touch) 
		#Logger.info('touch.pos:')
		#Logger.info(touch.pos)
		if touch.grab_current == self and len(self._touches) == 0:
			print self.map.parent.rotation
			rot = round((self.rotation - self.map.parent.rotation) / 90.0) * 90.0
			self.rotation = 0
			(x,y) = self._get_pos()
			print 'with rotation'
			print (x,y,self.rotation)
			(x,y) = self.map.to_widget(x,y)
			print (x,y)
			self.grid = (round(float(x) / 126.0), round(float(y) / 126.0))
			print self.grid
			#this call is required if the value of self.grid does not change
			self._set_to_grid(self.grid)
			self.rotation = rot + self.map.parent.rotation
			#Logger.info('rotation: %f',self.rotation)
			#Logger.info(self._get_center())
			#Logger.info(self._get_bbox())

		#Logger.info('touch_up')

	def _set_to_grid(self, grid_location):
		[x,y] = grid_location
		self.pos = self.map.to_window(x*126,y*126)
		print 'pos'
		print self.pos
		#self.rotation += self.map.rotation
		#Logger.info('tile.pos:')
		#Logger.info(self.pos)

	def resetTile(self, new_tile):
		self.tile = new_tile
		#update the tile image
		self.add_widget(new_tile.get_image())
		#move the widget to the next players position


