import random

def comp(card):
	return int(card.value)

class Card:
	suit = ""
	value = ""

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
		
class Deck:
	cards = []
	def __init__(self, new_deck = True):
		if (new_deck):
			for x in range(1, 15):
				self.cards.append(Card("C", str(x)))
				self.cards.append(Card("S", str(x)))
				self.cards.append(Card("H", str(x)))
				self.cards.append(Card("D", str(x)))

	def shuffle(self):
		new_deck = []
		for x in range(len(self.cards)):
			card = random.choice(self.cards)
			new_deck.append(card)
			self.cards.remove(card)
		self.cards = new_deck

	def draw(self):
		return self.cards.pop()

	def layout(self):
		"""
		Test method to see shuffled deck
		"""
		card_string = ""
		for card in self.cards:
			card_string += card.value + " "
		return card_string

	def add(self, card):
		self.cards.append(card)

	def clear(self):
		self.cards.clear()

class Hand:
	cards = []
	AI = True
	number = 0

	def __init__(self, number):
		self.cards = []
		self.number = number

	def size(self):
		return len(self.cards)

	def play(self, card_number):
		#print(str(self.number) + ": " + self.show_hand())
		card = self.cards.pop(card_number)
		#print(str(self.number) + ": " + self.show_hand())
		return card

	def skip(self):
		return Card("X", "0")

	def draw(self, card):
		self.cards.append(card)

	def show_hand(self):
		"""
		Test method to see shuffled deck
		"""
		card_string = ""
		for card in self.cards:
			card_string += "(" + card.value + "," + card.suit + "), "
		return card_string

	def decide(self):
		total = 0
		decision = False
		for card in self.cards:
			if int(card.value) > 10 and int(card.value) != 14:
				total += 10
			elif int(card.value) == 14:
				total += 11
			else:
				total += int(card.value)
		if self.AI:
			if total < 11:
				decision = True
		else:
			print(total)
			answer = input("Hit or stand? (h or s): ")
			if answer == "h":
				decision = True
		return decision
		
		# if int(top_card.value) == 0:
		# 	self.play(0)
		# else:
		# 	for card in self.cards:
		# 		if int(card.value) > int(top_card.value):
		# 			print("playing " + str(card.value))
		# 			return self.play(self.cards.index(card))
		# return self.skip()

	# def player_decides(self, top_card):
	# 	# print("The top card is: " + top_card.value + ". Your cards are:")
	# 	# print(self.show_hand())
	# 	# while True:
	# 	# 	number = input("Which card do you want to play? (0 - " + str(len(self.cards) - 1) + "), or 'x' to skip.")
	# 	# 	if number == 'x':
	# 	# 		return self.skip()
	# 	# 	if int(self.cards[int(number)].value) > int(top_card.value):
	# 	# 		return self.play(int(number))
	# 	# 	else:
	# 	# 		print("You must choose a card that is greater than the top card.")


	def is_AI(self):
		return self.AI

	def set_player(self):
		self.AI = False





# # print(deck.layout())
# deck.shuffle()
# # print(deck.layout())

# hand_one = Hand()
# hand_two = Hand()
# hand_three = Hand()
# hand_four = Hand()

# for x in range(1,14):
# 	hand_one.draw(deck.draw())
# 	hand_two.draw(deck.draw())
# 	hand_three.draw(deck.draw())
# 	hand_four.draw(deck.draw())

# hand_one.cards.sort(key=comp)
# hand_two.cards.sort(key=comp)
# hand_three.cards.sort(key=comp)
# hand_four.cards.sort(key=comp)

# print(hand_one.show_hand())
# print(hand_two.show_hand())
# print(hand_three.show_hand())
# print(hand_four.show_hand())