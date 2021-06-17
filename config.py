import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"

		#GAME CONFIG
		self.row = 5
		self.column = 5

		#WINDOW CONFIG
		base = 100
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+75"


		#IMG BUTTON PATH
		self.init_img_btn = "img/init_img.png"
		self.final_img_btn = "img/final_img.png"
		self.win_img_btn = "img/win_img.png"

		self.main_menu_logo_path = "img/main_menu.png"

		self.users_path = "json/users.json"

	def load_userData(self, users_path):
		with open(users_path, "r") as json_data:
			userData = json.load(json_data)
		return userData

	def load_data(self):
		pass

	def save_data(self):
		pass

	def login(self, username, password):
		users = self.load_userData(self.users_path)
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False