"""
A simple implementation of the rock paper scissor game using OOP.
"""

import random

class RockPaperScissor:
	def __init__(self):
		self.game_options = ["Rock", "Paper", "Scissor"]

	def play(self):
		"""Start the game"""
		while True:
			user = input("What do you choose? Type 0 for Rock,\n1 for Paper or 2 for Scissor\nq to stop playing\n")
			computer = random.randint(0, 2)
			if user.lower()=="q":
				return
			self.who_won(int(user), computer)

	def who_won(self, users, computers):
		"""check who won and print the result"""
		if users==computers:
			print(f"{self.game_options[users]} vs {self.game_options[computers]}?\n It's a Tie!")
		elif (users==0 and computers==2) or (users==1 and computers==0) or (users==2 and computers==1):
			print(f"{self.game_options[users]} vs {self.game_options[computers]}?\n You won!")
		else:
			print(f"{self.game_options[users]} vs {self.game_options[computers]}?\n You lost!")


rpc = RockPaperScissor()
rpc.play()