from constants.constants import SUIT_SYMBOLS


class Card:
    """ Card Class - Models a single Playing Card """

    def __init__(self, rank, suit):
        """ Class Constructor
		Args:
			rank: A valid RANK value - a single char
			suit: A valid SUIT value - a string
		Returns:
			No return value
		"""
        self.rank = rank
        self.suit = suit
        self.isjoker = False

    def __str__(self):
        """ Helper for builtin __str__ function
		Args:
			no args.
		Returns:
			string representation of the Card.  For Joker a "-J" is added.
			for example for 4 of Hearts, returns 4♡
				and if it is a Joker returns 4♡-J
		"""
        if self.isjoker:
            return self.rank + SUIT_SYMBOLS[self.suit] + '-J'
        return self.rank + SUIT_SYMBOLS[self.suit]

    def is_joker(self):
        """Status check to see if this Card is a Joker
		Args:
			no arguments
		Returns:
			True or False
		"""
        return self.isjoker
