"""Main"""
from kivy.app import App
from interface import Interface

class PianoTilesApp(App):
	"""Game Runner"""
	def build(self):
		return Interface()

if __name__ == '__main__':
	PianoTilesApp().run()
