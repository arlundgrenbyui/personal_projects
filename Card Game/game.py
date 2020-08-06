import card_class

class Game():
	players = []
	deck = ""
	discard = ""

	def __init__(self):
		self.deck = card_class.Deck()
		self.discard = card_class.Deck(False)
		for x in range(4):
			self.players.append(card_class.Hand(x))

	def deal(self):
		self.deck.shuffle()
		print(self.deck.layout())
		for x in range(1,3):
			for player in self.players:
				player.draw(self.deck.draw())
		# for player in self.players:
		# 	player.cards.sort(key=card_class.comp)

	def play(self):
		self.players[0].set_player()
		playing = True
		busted = []
		passed = []
		while playing:
			busted.clear()
			passed.clear()
			in_round = True
			totals = [0,0,0,0]
			showing = list()
			for player in self.players:
				showing.append(player.cards[0].value)
			while in_round:
				print("Showing card value for 0, 1, 2, and 3: ")
				print(showing)
				for player in self.players:
					if not player in busted and not player in passed:
						# print(player.show_hand())
						total = 0
						for card in player.cards:
							if int(card.value) > 10 and int(card.value) != 14:
								total += 10
							elif int(card.value) == 14:
								total += 11
							else:
								total += int(card.value)
						# print(total)
						if total > 21:
							print(str(player.number) + " busted!")
							print(player.show_hand())
							busted.append(player)
						if not player in busted and player.decide():
							print(str(player.number) + " drew a card.")
							player.draw(self.deck.draw())
						elif not player in busted:
							print(str(player.number) + " stands")
							passed.append(player)
							totals[player.number] = total
				if len(passed) + len(busted) == 4:
					in_round = False

			
			# for player in passed:
			# 	for card in player.cards:
			# 		totals[player.number] += int(card.value)
			# winner = self.players[0]
			# for player in totals:
			# 	if totals[player] > winner
			# 		winner = totals[player]
			print("0: " + str(totals[0]))
			print("1: " + str(totals[1]))
			print("2: " + str(totals[2]))
			print("3: " + str(totals[3]))
			windex = totals.index(max(totals))
			print("The winner is: " + str(windex))
			print(self.players[windex].show_hand())
			answer = input("Do you want to play again? (y/n): ")
			if answer == "n":
				playing = False
			else:
				for player in self.players:
					player.cards.clear()
					for x in range(2):
						player.draw(self.deck.draw())

		# self.players[0].set_player()
		# playing = True
		# winning_order = []
		# round_order = []
		# in_round = self.players
		# winner = card_class.Hand(0)
		# while playing:
		# 	playing_round = True
		# 	self.discard.add(card_class.Card("X", "0"))
		# 	while playing_round:
		# 		print("New Round!")
		# 		for player in in_round:
		# 			print(str(player.number))
		# 		for player in self.players:
		# 			if player in in_round:
		# 				if player.is_AI():
		# 					print(str(player.number) + ": ")
		# 					card = player.decide(self.discard.cards[-1])
		# 					print(card.value)
		# 					if card.value != "0":
		# 						self.discard.add(card)
		# 						if len(player.cards) == 0:
		# 							if winner.number != 0:
		# 								winning_order.append(player)
		# 								in_round.remove(player)
		# 					else:
		# 						round_order.append(player)
		# 						in_round.remove(player)
		# 				else:
		# 					card = player.player_decides(self.discard.cards[-1])
		# 					print(card.value)
		# 					if card.value != "0":
		# 						self.discard.add(card)
		# 						if len(player.cards) == 0:
		# 							if winner.number != 0:
		# 								winning_order.append(player)
		# 								in_round.remove(player)
		# 					else:
		# 						round_order.append(player)
		# 						in_round.remove(player)


		# 		if len(in_round) < 2:
		# 			round_order.append(self.players)
		# 			in_round = []
		# 			round_order.append(winner)
		# 			round_order.reverse()
		# 			in_round = round_order
		# 			playing_round = False

		# 		num_with_cards = 0

		# 		if len(in_round) > 1:
		# 			for player in in_round:
		# 				if type(player) is list:
		# 					if player[0].size() > 0:
		# 						num_with_cards += 1
		# 				elif player.size() > 0:
		# 					num_with_cards += 1

		# 		if num_with_cards <= 1:
		# 			playing = False
				

		# for player in winning_order:
		# 	print(player.number)

			# self.discard.remove(0)
			# self.discard.shuffle()
			# self.discard

def main():
	game = Game()
	print("Game initialized")
	game.deal()
	print("Cards dealt")
	game.play()

if __name__ == "__main__":
	main()