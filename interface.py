"""Interface"""
import sys
from functools import partial
from random import choice

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Line, Rectangle, Color
from kivy.uix.label import Label
from kivy.clock import Clock

from tiles import TileBlock

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
		self.create_tiles()

	def all_variables(self):
		"""All Variables"""
		self.index_of_tiles = 0
		self.selection = 0
		self.speed_of_tile = 20

	def divider(self):
		"""Line Divider"""
		self.canvas.add(Color(rgba = (0, 0, 1, 1)))
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
		self.all_tiles[self.index_of_tiles].on_press= (
		partial(
		self.touched_tile, self.index_of_tiles))

		self.tiles_clock.append(
		Clock.schedule_interval(
		partial(
		self.move_tiles, self.index_of_tiles), 1/60))
		self.speed_of_tile += 0.0
		self.index_of_tiles += 1

	def all_menu_choice(self):
		"""All Menu Choices"""
		if self.selection == 1:
			return [
			self.width * 0.25,
			self.width * 0.50,
			self.width * 0.75]
		if self.selection == 2:
			return [
			self.width * 0,
			self.width * 0.50,
			self.width * 0.75]
		if self.selection == 3:
			return [
			self.width * 0,
			self.width * 0.25,
			self.width * 0.75]
		if self.selection == 4:
			return [
			self.width * 0,
			self.width * 0.25,
			self.width * 0.50]
		return [
		self.width * 0,
		self.width * 0.25,
		self.width * 0.50,
		self.width * 0.75]

	def move_tiles(self, index, delta_time):
		"""Move the Tiles"""
		#pylint:disable=W0613
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
		- self.height * 0.2):
			if self.check_press_tile_boolean[index]:
				self.tiles_clock[index].cancel()
				self.remove_widget(
				self.all_tiles[index])
			else:
				sys.exit()

	def touched_tile(self, index):
		"""Check if Touch"""
		if index != 0:
			if self.check_press_tile_boolean[
			index-1] is False:
				sys.exit()
		self.all_tiles[index].opacity = 0.1
		self.check_press_tile_boolean[index] = True



class InterfaceApp(App):
	"""Interface App"""
	def build(self):
		return Label(text = "Interface Class")

if __name__ == '__main__':
	InterfaceApp().run()
