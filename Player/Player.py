from Functions import print_cards
from Functions import get_object
from Functions import sort_sequence




class Player:
    """ Player Class - Models Players Hand and play actions """

    def __init__(self, name, deck, game):
        """ Class Constructor
		Args:
			name: Name of the Player - string
			deck: Reference to the Deck Object that is part of the Game
			game: Reference to the Game object that is being played now
		Returns:
			No return value
		"""
        self.stash = []  # Stash represents the hand of the Player.
        self.name = name
        self.deck = deck
        self.game = game

    def deal_card(self, card):
        """ Deal a Card to the Player
		Args:
			card:  The Card object provided to Player as part of the deal
		Returns:
			No returns
		"""
        try:
            self.stash.append(card)
            if len(self.stash) > 14:
                raise ValueError('ERROR: Player cannot have more than 14 cards during turn')
        except ValueError as err:
            print(err.args)

    def drop_card(self, card):
        """ Drop Card operation by the Player
		Args:
			card: The player input representation of the Card object
				that needs to be dropped.  For example: AC for Ace of Clubs
		Returns:
			No returns
		"""
        # Get the actual card object from string representation
        card = get_object(self.stash, card)

        # Cannot drop a card if it is already not in stash
        if card not in self.stash:
            return False

        self.stash.remove(card)

        # Player dropped card goes to Pile
        self.game.add_pile(card)

        return True

    def close_game(self):
        """ Close Game operation by the Player
		Args:
			No args
		Returns:
			Success or Failure as True/False
		"""
        # Divide the stash into 4 sets, 3 sets of 3 cards and 1 set of 4 cards
        set_array = [self.stash[:3], self.stash[3:6], self.stash[6:9], self.stash[9:]]

        # Need to count the number of sets that are runs without a joker.
        # 	There must be at least one run with out a joker
        count = 0
        for s in set_array:
            if is_valid_run(s):
                count += 1
        if count == 0:
            return False

        # Check if each of the sets is either a run or a book
        for s in set_array:
            if is_valid_run(s) is False and is_valid_book(s) is False and is_valid_run_joker(s) is False:
                return False

        return True

    def play(self):
        """ Play a single turn by the Player
		Args:
			No args
		Returns:
			Success or Failure as True/False
		"""
        # Stay in a loop until the Player drops a card or closes the game.
        while True:
            # clear screen to remove the output of previous Player action
            print(chr(27) + "[2J")
            print("***", self.name, "your cards are:")
            print(print_cards(self.stash))
            self.game.display_pile()

            # Get Player Action
            action = input(
                "*** " + self.name + ", What would you like to do? ***, \n(M)ove Cards, (P)ick from pile, (T)ake from deck, (D)rop, (S)ort, (C)lose Game, (R)ules: ")

            # Move or Rearrange Cards in the stash
            if action == 'M' or action == 'm':
                lp = 1
                while int(lp):
                    # Get the Card that needs to moved.
                    move_what = input("Enter which card you want to move i.e. 4H (4 of Hearts): ")
                    move_what.strip()
                    if get_object(self.stash, move_what.upper()) not in self.stash:
                        input("ERROR: That card is not in your stash.  Enter to continue")
                        continue

                    # Get the Card where the move_what needs to moved.
                    move_where = input(
                        "Enter where you want move card to (which card the moving card will go before) Enter Space to move to end \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts):")
                    move_where.strip()
                    if move_where != "" and get_object(self.stash, move_where.upper()) not in self.stash:
                        input("ERROR: This is an invalid location.  Enter to continue")
                        continue

                    # Perform the Move Operation
                    move_what = get_object(self.stash, move_what.upper())
                    if move_where != "":
                        move_where = get_object(self.stash, move_where.upper())
                        location = self.stash.index(move_where)
                        if location > self.stash.index(move_what):
                            location = location - 1
                        self.stash.remove(move_what)
                        self.stash.insert(location, move_what)
                    else:
                        # If the move_where was not specified by the User then,
                        #the card to the end of the stash
                        self.stash.remove(move_what)
                        self.stash.append(move_what)
                    print(print_cards(self.stash))
                    lp = input("Type 0 to exit move:")
                    if lp == "":
                        lp = 1

            # Pick card from Pile
            if action == 'P' or action == 'p':
                if len(self.stash) < 14:
                    c = self.game.draw_pile()
                    self.stash.append(c)
                else:
                    input("ERROR: You have " + str(len(self.stash)) + " cards. Cannot pick anymore. Enter to continue")

            # Take Card from Deck
            if action == 'T' or action == 't':
                if len(self.stash) < 14:
                    c = self.deck.draw_card()
                    self.stash.append(c)
                else:
                    input("ERROR: You have " + str(len(self.stash)) + " cards. Cannot take anymore. Enter to continue")

            # Drop card to Pile
            if action == 'D' or action == 'd':
                if len(self.stash) == 14:
                    drop = input(
                        "Which card would you like to drop? \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
                    drop = drop.strip()
                    drop = drop.upper()
                    if self.drop_card(drop):
                        # return False because Drop Card does not end the game
                        return False
                    else:
                        input("ERROR: Not a valid card, Enter to continue")
                else:
                    input("ERROR: Cannot drop a card. Player must have 13 cards total. Enter to continue")

            # Sort cards in the stash
            if action == 'S' or action == 's':
                sort_sequence(self.stash)

            # Close the Game
            if action == 'C' or action == 'c':

                if len(self.stash) == 14:
                    drop = input(
                        "Which card would you like to drop? \nEnter Rank followed by first letter of Suit. i.e. 4H (4 of Hearts): ")
                    drop = drop.strip()
                    drop = drop.upper()
                    if self.drop_card(drop):
                        if self.close_game():
                            print(print_cards(self.stash))
                            # Return True because Close ends the Game.
                            return True
                        else:
                            input("ERROR: The game is not over. Enter to Continue playing.")
                            # if this Close was false alarm then discarded Card will
                            #		have to be put back into the stash for the Player to continue.
                            self.stash.append(self.game.draw_pile())
                    else:
                        input("ERROR: Not a valid card, Enter to continue")
                else:
                    input("ERROR: You do not have enough cards to close the game. Enter to Continue playing.")

            # Show Rules of the game
            if action == 'R' or action == 'r':
                print("------------------ Rules --------------------",
                      "\n- Rummy is a card game based on making sets.",
                      "\n- From a stash of 13 cards, 4 sets must be created (3 sets of 3, 1 set of 4).",
                      "\n- The set of 4 must always be at the end"
                      "\n- A valid set can either be a run or a book.",
                      "\n- One set must be a run WITHOUT using a joker."
                      "\n- A run is a sequence of numbers in a row, all with the same suit. ",
                      "\n \tFor example: 4 of Hearts, 5 of Hearts, and 6 of Hearts",
                      "\n- A book of cards must have the same rank but may have different suits.",
                      "\n \tFor example: 3 of Diamonds, 3 of Spades, 3 of Clubs",
                      "\n- Jokers are randomly picked from the deck at the start of the game.",
                      "\n- Joker is denoted by '-J' and can be used to complete sets.",
                      "\n- During each turn, the player may take a card from the pile or from the deck.",
                      "Immediately after, the player must drop any one card into the pile so as not go over the 13 card limit.",
                      "\n- When a player has created all the sets, select Close Game option and drop the excess card into the pile.",
                      "\n- Card with Rank 10 is represented as Rank T"
                      "\n--------------------------------------------")
                input("Enter to continue ....")