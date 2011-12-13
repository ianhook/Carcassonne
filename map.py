from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget

class Map(FloatLayout):

	scatter = Scatter(auto_bring_to_front=False,do_scale=False,do_rotation=False)

	def addPiece(self, piece, piece_pos):
		print 'Map::addPiece'
		print piece_pos
		#image = Widget(pos=piece_pos,size=(126,126))
		#image.add_widget(piece.get_image())
		image = piece.get_image()
		image.pos = piece_pos
		image.size=self.tileSet.size
		image.size_hint=(.25,.25)
		self.add_widget(image)

	def getDisplayRoot(self):
		print self.scatter.center
		print self.scatter.size
		self.scatter.size = self.size
		self.center = self.scatter.center
		self.scatter.add_widget(self)
		return self.scatter

	def expand(self,x,y):
		pass
