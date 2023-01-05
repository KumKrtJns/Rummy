from Player import Player


class Game:
    """ Game Class - Models a single Game """

    def __init__(self, hands, deck):
        """ Class Constructor
			Args:
				hands:  represents the number of players in the game - an int
				deck: Reference to Deck Object
			Returns:
				No returns
		"""
        self.pile = []
        self.players = []

        for i in range(hands):
            name = input("Enter name of Player " + str(i) + ": ")
            self.players.append(Player(name, deck, self))

    def display_pile(self):
        """ Displays the top of the Pile.
			Args:
				No args.
			Returns:
				No returns
		"""
        if len(self.pile) == 0:
            print("Empty pile.")
        else:
            print("The card at the top of the pile is: ", self.pile[0])

    def add_pile(self, card):
        """ Adds card to the top of the Pile.
			Args:
				card:  The card that is added to top of the Pile
			Returns:
				No returns
		"""
        self.pile.insert(0, card)

    def draw_pile(self):
        """ Draw the top card from the Pile.
			Args:
				No args
			Returns:
				Returns the top Card from the Pile - Card Object
		"""
        if len(self.pile) != 0:
            return self.pile.pop(0)
        else:
            return None

    def play(self):
        """ Play the close_game.
			Args:
				No args
			Returns:
				No returns
		"""
        i = 0
        while not self.players[i].play():
            # clear screen to remove the output of previous Player action
            print(chr(27) + "[2J")
            i += 1
            if i == len(self.players):
                i = 0
            print("***", self.players[i].name, "to play now.")

        # Game Over
        print("*** GAME OVER ***")
        print("*** ", self.players[i].name, " Won the game ***")


if __name__ == "__main__":
    pass
