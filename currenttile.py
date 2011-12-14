'''
Current Tile
============

This module does all of the game work.  The main program loop is created in the kivy framework behind the scenes so we only need to worry about how user input will update the screen.  For turn based games like this one it's easy enough to wait for input events and then update the screen in response.

For games with real time events a clock function will need to be used to update the screen regardless of user events. I'm not sure how this will work yet.
'''
from kivy.uix.scatter import Scatter
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.logger import Logger

class CurrentTile(Scatter):
	
	grid = ListProperty([1, 2])

	def __init__(self, **kwargs):
		Logger.info('hi')
		kwargs.setdefault('do_scale', False)
		print 'size'
		print self.tile_size
		kwargs.setdefault('size', self.tile_size)
		super(CurrentTile, self).__init__(**kwargs)
		self.grid_trigger = Clock.create_trigger(self._set_to_grid)
		self.bind(grid=self.grid_trigger)

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
			print  round(float(x) / self.tile_size[0]), round(float(y) / self.tile_size[1])
			self.grid = round(float(x) / self.tile_size[0]), round(float(y) / self.tile_size[1])
			#this call is required if the value of self.grid does not change
			self.grid_trigger(self.grid)
			self.rotation = rot + self.map.parent.rotation
			#Logger.info('rotation: %f',self.rotation)
			#Logger.info(self._get_center())
			#Logger.info(self._get_bbox())

		#Logger.info('touch_up')

	def _set_to_grid(self, *largs):
		[x,y] = self.grid
		self.pos = self.map.to_window(x*self.tile_size[0],y*self.tile_size[1])

	def resetTile(self, new_tile):
		self.tile = new_tile
		#update the tile image
		self.add_widget(new_tile.get_image())
		#move the widget to the next players position

