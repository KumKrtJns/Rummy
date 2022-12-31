def unit_tests():
    """ Unit Tests for Checking various aspects of the program
		Args:
			No args
		Returns:
			no returns.
	"""

    print("Running Unit Tests")
    """
	#test 1 - check players deal card exception handling
	player = Player("Vinitha", None, None)
	player.deal_card(Card("4", "Hearts"))
	player.deal_card(Card("5", "Hearts"))
	player.deal_card(Card("6", "Hearts"))
	player.deal_card(Card("5", "Spades"))
	player.deal_card(Card("5", "Diamonds"))
	player.deal_card(Card("5", "Clubs"))
	player.deal_card(Card("J", "Clubs"))
	player.deal_card(Card("7", "Diamonds"))
	player.deal_card(Card("8", "Spades"))
	player.deal_card(Card("3", "Diamonds"))
	player.deal_card(Card("A", "Spades"))
	player.deal_card(Card("2", "Clubs"))
	player.deal_card(Card("A", "Hearts"))
	player.deal_card(Card("9", "Spades"))
	player.deal_card(Card("9", "Hearts"))

	"""

    # test 2 - check close game
    player1 = Player("Vinitha", None, None)
    player1.deal_card(Card("4", "Hearts"))
    player1.deal_card(Card("5", "Hearts"))
    player1.deal_card(Card("6", "Hearts"))
    player1.deal_card(Card("5", "Spades"))
    player1.deal_card(Card("5", "Diamonds"))
    player1.deal_card(Card("5", "Clubs"))
    player1.deal_card(Card("J", "Clubs"))
    player1.deal_card(Card("J", "Hearts"))
    player1.deal_card(Card("J", "Spades"))
    player1.deal_card(Card("5", "Diamonds"))
    player1.deal_card(Card("2", "Diamonds"))
    player1.deal_card(Card("3", "Diamonds"))
    player1.deal_card(Card("4", "Diamonds"))
    assert (player1.close_game() == True)

    player2 = Player("Varun", None, None)
    player2.deal_card(Card("2", "Diamonds"))
    player2.deal_card(Card("3", "Hearts"))
    player2.deal_card(Card("4", "Hearts"))
    player2.deal_card(Card("4", "Clubs"))
    player2.deal_card(Card("4", "Diamonds"))
    player2.deal_card(Card("8", "Clubs"))
    player2.deal_card(Card("9", "Clubs"))
    player2.deal_card(Card("T", "Clubs"))
    player2.deal_card(Card("J", "Clubs"))
    player2.deal_card(Card("K", "Spades"))
    player2.deal_card(Card("A", "Hearts"))
    player2.deal_card(Card("K", "Hearts"))
    player2.deal_card(Card("K", "Spades"))
    assert (player2.close_game() == False)

    """
	#test 3 - testing ace values
	player3 = Player("Narm", None, None)
	player3.deal_card(Card("K", "Diamonds"))
	player3.deal_card(Card("Q", "Diamonds"))
	player3.deal_card(Card("J", "Diamonds"))
	player3.deal_card(Card("A", "Diamonds"))
	sort_sequence(player3.stash)
	print(print_cards(player3.stash))


	#test 4 - testing joker in a book
	player4 = Player("Vatsala", None, None)
	player4.deal_card(Card("A", "Spades"))
	player4.deal_card(Card("6", "Diamonds"))
	player4.deal_card(Card("6", "Clubs"))
	player4.deal_card(Card("6", "Hearts"))
	player4.stash[0].isjoker=True
	assert (is_valid_book(player4.stash) == True)

	#test 5 - testing joker in a run
	player5 = Player("Tom", None, None)
	player5.deal_card(Card("3", "Diamonds"))
	player5.deal_card(Card("A", "Diamonds"))
	player5.deal_card(Card("7", "Hearts"))
	player5.deal_card(Card("4", "Diamonds"))
	#player5.stash[0].isjoker=True
	player5.stash[2].isjoker=True
	print(print_cards(player5.stash))
	assert (is_valid_run_joker(player5.stash) == True)

	#test 6 - testing is_valid_run
	player6 = Player("Tom", None, None)
	player6.deal_card(Card("J", "Diamonds"))
	player6.deal_card(Card("A", "Diamonds"))
	player6.deal_card(Card("Q", "Diamonds"))
	player6.deal_card(Card("K", "Diamonds"))
	print(print_cards(player6.stash))
	assert (is_valid_run(player6.stash) == True)


	#test 7 - testing push_joker_toend function
	player7 = Player("Tom", None, None)
	player7.deal_card(Card("A", "Spades"))
	player7.deal_card(Card("6", "Diamonds"))
	player7.deal_card(Card("7", "Hearts"))
	player7.deal_card(Card("9", "Diamonds"))
	player7.stash[0].isjoker=True
	player7.stash[2].isjoker=True
	print(print_cards(player7.stash))
	push_joker_toend(player7.stash)
	print(print_cards(player7.stash))
	"""