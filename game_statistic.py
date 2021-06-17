import time

class Game_Statistic:

	def __init__(self):
		#SCORE BOARD
		self.win = False #Flag / Sign
		self.score = 0
		self.steps = 0
		self.start = None
		self.finish = None