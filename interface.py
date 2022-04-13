"""Interface"""
#import sys
from functools import partial
from random import choice, randint

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Line, Rectangle, Color
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.metrics import sp

from tiles import TileBlock

LabelBase.register(
name = "EvilEmpire",
fn_regular = "EvilEmpire-4BBVK.ttf")

class Interface(Widget):
	"""Interface"""
	line_area = [ ]
	all_tiles = [ ]
	tiles_clock = [ ]
	tile_boolean = [ ]
	check_press_tile_boolean = [ ]

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.width = Window.width
		self.height = Window.height
		self.all_variables()
		self.divider()
		self.start_tile()

	def start_tile(self):
		"""First Tile"""
		menu_choice = self.all_menu_choice()
		been_choose = choice(menu_choice)
		self.starter_tile = TileBlock()
		self.starter_tile.size = (
		self.width * 0.25, self.height * 0.2)
		self.starter_tile.pos = (
		been_choose, self.height * 0.1)

		self.starter_tile_2 = TileBlock()
		self.starter_tile_2.size = (
		self.width * 0.25, self.height * 0.2)
		self.starter_tile_2.pos = (
		been_choose, self.height * 0.1)

		self.start_text = Label()
		self.start_text.text = "Start"
		self.start_text.font_name = "EvilEmpire"
		self.start_text.font_size = sp(32)
		self.start_text.pos = (

		# X
		been_choose + ((
		self.width * 0.25)/2) - (
		self.start_text.size[0]/2),
		# Y
		(self.height * 0.1) + ((
		self.height * 0.2)/2) - (
		self.start_text.size[1]/2))


		self.starter_tile.on_press = self.start_game
		self.add_widget(self.starter_tile_2)
		self.add_widget(self.starter_tile)
		self.add_widget(self.start_text)

	def start_game(self):
		"""Start Game"""
		self.create_tiles()
		self.remove_widget(self.starter_tile)
		self.remove_widget(self.start_text)
		self.starter_tile_2.opacity = 0.1
		self.starter_clock = Clock.schedule_interval(
		lambda dt: self.move_start_tile(), 1/60)
		self.score()

	def move_start_tile(self):
		"""Move Start Tile"""
		self.starter_tile_2.pos = (
		self.starter_tile_2.pos[0],
		self.starter_tile_2.pos[1] - (
		self.speed_of_tile))
		if self.starter_tile_2.pos[1] < (
		- self.height * 0.2):
			self.starter_clock.cancel()
			self.remove_widget(self.starter_tile_2)

	def all_variables(self) -> None:
		"""All Variables"""
		self.index_of_tiles = 0
		self.selection = 0
		self.stop_move = False
		self.speed_of_tile = 10
		self.score_value = 0

	def divider(self) -> None:
		"""Line Divider"""
		self.canvas.add(Color(rgba = (
			178/255, 235/255, 247/255, 1)))
		self.background = Rectangle()
		self.background.size = (
			self.width, self.height)
		self.canvas.add(self.background)
		self.canvas.add(Color(rgba = (1, 1, 1, 1)))

		width_of_line = 0
		for line in range (5):
			self.line_area.append(Line())
			self.line_area[line].points = (
			0 + self.width * width_of_line, 0,
			0 + self.width * width_of_line,
			self.height)
			self.canvas.add(self.line_area[line])
			width_of_line += 0.25
		self.line_perfect_zone = Line()
		self.line_perfect_zone.width = 2
		self.line_perfect_zone.points = (
		0, self.height * 0.2,
		self.width, self.height * 0.2)
		self.canvas.add(self.line_perfect_zone)

	def create_tiles(self):
		"""Create Tiles"""
		menu_choice = self.all_menu_choice()
		been_choose = choice(menu_choice)
		if been_choose == 0:
			self.selection = 1
		elif been_choose == self.width * 0.25:
			self.selection = 2
		elif been_choose == self.width * 0.50:
			self.selection = 3
		elif been_choose == self.width * 0.75:
			self.selection = 4
		self.tile_boolean.append(False)
		self.all_tiles.append(TileBlock())
		self.all_tiles[self.index_of_tiles].size = (
		self.width * 0.25, self.height * 0.2)
		self.all_tiles[self.index_of_tiles].pos = (
		been_choose, self.height)
		self.add_widget(
		self.all_tiles[self.index_of_tiles])

		self.check_press_tile_boolean.append(False)
		self.all_tiles[self.index_of_tiles].on_press = (
		partial(self.touched_tile, self.index_of_tiles))

		self.tiles_clock.append(
		Clock.schedule_interval(
		partial(
		self.move_tiles, self.index_of_tiles), 1/60))
		self.speed_of_tile += 0.05
		self.index_of_tiles += 1

	def all_menu_choice(self) -> "return choices":
		"""All Menu Choices"""
		if self.selection == 1:
			return [self.width * 0.25,
			self.width * 0.50,
			self.width * 0.75]
		if self.selection == 2:
			return [self.width * 0,
			self.width * 0.50,
			self.width * 0.75]
		if self.selection == 3:
			return [self.width * 0,
			self.width * 0.25,
			self.width * 0.75]
		if self.selection == 4:
			return [self.width * 0,
			self.width * 0.25,
			self.width * 0.50]
		return [self.width * 0,
		self.width * 0.25,
		self.width * 0.50,
		self.width * 0.75]

	def move_tiles(self, index, delta_time):
		"""Move the Tiles"""
		#pylint:disable=W0613
		self.remove_widget(self.score_text)
		self.score_text.text = str(self.score_value)
		self.add_widget(self.score_text)
		if self.stop_move:
			return
		self.all_tiles[index].pos = (
		self.all_tiles[index].pos[0],
		self.all_tiles[index].pos[1] - (
		self.speed_of_tile))

		if self.all_tiles[index].pos[1] < (
		self.height * 0.8):
			if self.tile_boolean[index] is False:
				self.tile_boolean[index] = True
				self.create_tiles()
		if self.all_tiles[index].pos[1] < (
		- self.height * 0.3):
			if self.check_press_tile_boolean[index]:
				self.tiles_clock[index].cancel()
				self.remove_widget(
				self.all_tiles[index])
			else:
				#sys.exit()
				self.lose_interface()
				self.stop_move = True

	def touched_tile(self, index):
		"""Check if Touch"""
		if self.stop_move:
			return
		if index != 0:
			if self.check_press_tile_boolean[
			index-1] is False:
				self.all_tiles[index].color = (
				1, 0, 0, 1)
				self.lose_interface()
				self.stop_move = True
		self.all_tiles[index].opacity = 0.1
		self.check_press_tile_boolean[index] = True
		self.score_value += randint(3, 6)

	def lose_interface(self):
		"""Pop Up When Lose"""
		self.lose_text = Label()
		self.lose_text.color = (1, 0, 0, 1)
		self.lose_text.font_size = sp(48)
		self.lose_text.text = "YOU LOSE"
		self.lose_text.font_name = "EvilEmpire"
		self.lose_text.pos = (
		(self.width/2) - (self.lose_text.size[0]/2),
		self.height/2)
		self.add_widget(self.lose_text)

	def score(self):
		"""Player Score"""
		self.score_text = Label()
		self.score_text.color = (3/255, 157/255, 252/255, 1)
		self.score_text.font_size = sp(48)
		self.score_text.text = "0"
		self.score_text.font_name = "EvilEmpire"
		self.score_text.pos = (
		(self.width/2) - (self.score_text.size[0]/2),
		self.height * 0.9)
		self.add_widget(self.score_text)

class InterfaceApp(App):
	"""Interface App"""
	def build(self):
		return Label(text = "Interface Class",
			font_name = "EvilEmpire",
			font_size = sp(32))

if __name__ == '__main__':
	InterfaceApp().run()
