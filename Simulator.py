from Game import Game

class Simulator:
	def __init__(self, agent_x, agent_y):
		self.game = Game()
		self.agent_x = agent_x
		self.agent_y = agent_y

	def start(self):
		while not self.game.is_over():
			game = self.game
			print()
			print(game.ascii())
			print(f"Turn: {game.turn.upper()}")

			action = -1
			if game.turn == 'x':
				action = self.agent_x.policy(game)
			else:
				action = self.agent_y.policy(game)

			self.game = game.action(action)
			print(f"Action chosen: {action}")

		score_x = self.game.score('x')
		score_y = self.game.score('y')

		message = "It's a draw!"
		if score_x > score_y: message = "Winner: X"
		if score_x < score_y: message = "Winner: Y"

		print()
		print(self.game.ascii())
		print(f"Game over! {message}")
