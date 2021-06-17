import tkinter as tk

class PlayAgain(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="white")
		self.main_frame.pack(expand=True)

		#BUTTON
		self.btn_play_again = tk.Button(self.main_frame, text="Play Again?", font=("Arial", 18, "bold"), command=lambda:self.game.create_board())
		self.btn_play_again.pack(pady=5)

		self.btn_main_menu = tk.Button(self.main_frame, text="Main Menu", font=("Arial", 18, "bold"), command=lambda:self.game.change_page('main_menu'))
		self.btn_main_menu.pack(pady=5)

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 18, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(pady=5)