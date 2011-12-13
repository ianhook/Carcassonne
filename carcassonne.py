from kivy.app import App
from kivy.factory import Factory
from kivy.logger import Logger
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from tileimage import TileImage
from currenttile import CurrentTile
from TileFactory import TileFactory
from map import Map

class CarcassonneApp(App):
	
	def build(self):
		#create window
		root = Widget()
		root.size = Window.size
		root.center = Window.center

		#create map
		Map.tileSet = TileFactory
		board = Map(size=(504,504))
		root.add_widget(board.getDisplayRoot())

		#add starting tile
		tile_fact = TileFactory()
		for i in range(1):
			btn = tile_fact.newTile(board)
			board.addPiece(btn,(i*126,i*126))

		#create players
		CurrentTile.map = board
		CurrentTile.size = TileFactory.size

		playerTile = CurrentTile(grid=[1,1])
	
		newTile = tile_fact.newTile(board)
		root.add_widget(playerTile)

		playerTile.resetTile(newTile)

		return root

if __name__ == '__main__':
	Factory.register('TileImage', TileImage)
	#Factory.register('Tile', Tile)
	CarcassonneApp().run()
