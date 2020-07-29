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

class Hand:
	cards = []

	def __init__(self):
		self.cards = []

	def play(self, card_number):
		return cards.pop(card_number)

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

deck = Deck()

# print(deck.layout())
deck.shuffle()
# print(deck.layout())

hand_one = Hand()
hand_two = Hand()
hand_three = Hand()
hand_four = Hand()

for x in range(1,14):
	hand_one.draw(deck.draw())
	hand_two.draw(deck.draw())
	hand_three.draw(deck.draw())
	hand_four.draw(deck.draw())

hand_one.cards.sort(key=comp)
hand_two.cards.sort(key=comp)
hand_three.cards.sort(key=comp)
hand_four.cards.sort(key=comp)

print(hand_one.show_hand())
print(hand_two.show_hand())
print(hand_three.show_hand())
print(hand_four.show_hand())