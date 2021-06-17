import tkinter as tk
import sys

from config import Config
from game_statistic import Game_Statistic
from ship import Ship
from player import Player
from board import Board
from main_menu import MainMenu
from login_page import LoginPage
from play_again import PlayAgain

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_main_menu()
		self.create_play_again()
		self.create_login_page()


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_login_page(self):
		self.pages['login_page'] = LoginPage(self.container, self)

	def create_main_menu(self):
		self.pages['main_menu'] = MainMenu(self.container, self)

	def create_play_again(self):
		self.pages['play_again'] = PlayAgain(self.container, self)

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def auth_login(self):
		username = self.pages['login_page'].var_username.get()
		password = self.pages['login_page'].var_password.get()

		granted = self.config.login(username, password)
		if granted:
			self.change_page('main_menu')


	def exit(self):
		sys.exit()


class Battleship:

	def __init__(self):
		self.config = Config()
		self.game_statistic = Game_Statistic()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			print("You Win!!!")
			#self.window.destroy()
			self.window.change_page('play_again')

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()