"""Tile"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

class TileBlock(ButtonBehavior, Image):
	""""TileBlock"""
	
class TileApp(App):
	"""Tile App"""
	def build(self):
		return Label(text = "Tile Class")

if __name__ == '__main__':
	TileApp().run()
