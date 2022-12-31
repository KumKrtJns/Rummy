import random
from constants.constants import SUIT, RANK
from Card import Card

class Deck:
    """ Deck Class - Models the card Deck """

    def __init__(self, packs):
        """ Class Constructor
		Args:
			packs: Number of packs used to create the Deck - int value
		Returns:
			No return value
		"""
        self.packs = packs
        self.cards = []
        self.joker = None

        # Create all cards in the Deck
        for i in range(packs):
            for s in SUIT:
                for r in RANK:
                    self.cards.append(Card(r, s))

    def shuffle(self):
        """ Shuffle the Deck, so that cards are ordered in a random order
		Args:
			No args
		Returns:
			No return value
		"""
        random.shuffle(self.cards)

    def draw_card(self):
        """ Draw a card from the top of the Deck
		Args:
			No args
		Returns:
			a Card Object
		"""
        a = self.cards[0]
        self.cards.pop(0)
        return a

    def set_joker(self):
        """ Set the Joker Cards in the Deck
		A Card is selected at random from the deck as Joker.
		All cards with the same Rank as the Joker are also set to Jokers.
		Args:
			No args
		Returns:
			No returns
		"""
        self.joker = random.choice(self.cards)

        # remove the Joker from Deck and display on Table for Players to see
        self.cards.remove(self.joker)

        for card in self.cards:
            if self.joker.rank == card.rank:
                card.isjoker = True