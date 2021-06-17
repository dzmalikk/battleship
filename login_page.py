import tkinter as tk
from PIL import Image, ImageTk


class LoginPage(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="light blue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="light blue")
		self.main_frame.pack(expand=True)

		self.group = tk.Label(self.main_frame,text="Brenden Kenley Efendy & M Dzaki Irsyadul Malik\n10 Komputer 1", font=("Arial",13, "bold"),bg="light blue",fg="black")
		self.group.pack(pady=5)

		self.label_username = tk.Label(self.main_frame, text="username", font=("Arial", 18, "bold"), bg="light blue", fg="black")
		self.label_username.pack(pady=5)

		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable=self.var_username)
		self.entry_username.pack(pady=5)

		self.label_password = tk.Label(self.main_frame, text="password", font=("Arial", 18, "bold"), bg="light blue", fg="black")
		self.label_password.pack(pady=5)

		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*", textvariable=self.var_password)
		self.entry_password.pack(pady=5)

		self.btn_login = tk.Button(self.main_frame, text="LOGIN", font=("Arial", 18, "bold"), command=lambda:self.game.auth_login())
		self.btn_login.pack(pady=5)

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 18, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(pady=5)