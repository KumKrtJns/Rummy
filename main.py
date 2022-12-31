#!/usr/bin/python3

#from package import function
from Deck import Deck
from Game import Game
"""
Author: Kumar
This program is for the card game Rummy.
MIT License

Rules:
- Rummy is a card game based on making sets.
- From a stash(or hand) of 13 cards, 4 sets must be created (3 sets of 3, 1 set of 4).
- A valid set can either be a run or a book.
- One set must be a run WITHOUT using a joker.
- A run is a sequence of numbers in a row, all with the same suit.
	For example: 4 of Hearts, 5 of Hearts, and 6 of Hearts
- A book is a set in which the cards all have the same rank but must have different suits.
	For example: 3 of Diamonds, 3 of Spades, 5 of Clubs
- A joker is a card randomly picked from the deck at the start of the game.
- All jokers are considered free cards and can be used to complete sets.
- During each player's turn, the player may take a card from the pile or a card from the deck to help create sets.
  Immediately after, the player must drop a card into the pile so as not go over the 14 card limit.
- When a player has created all the sets, select the close game option and drop the excess card into the pile.
- Card with Rank 10 is represented as Rank T
"""
def main():
    """ Main Program """

    # Create Deck with 3 Packs
    deck = Deck(1)
    deck.shuffle()

    # Joker Logic is disabled currently.
    # deck.set_joker()

    # New game with 1 players
    g = Game(1, deck)

    # Deal Cards
    for i in range(13):
        for hand in g.players:
            card = deck.draw_card()
            hand.deal_card(card)

    # Create Pile
    first_card = deck.draw_card()
    g.add_pile(first_card)

    # Now let the Players begin
    g.play()


if __name__ == "__main__":
    main()
