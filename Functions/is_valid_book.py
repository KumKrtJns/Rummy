def is_valid_book(sequence):
    """ Check if the sequence is a valid book.
		Args:
			sequence: an array of Card objects.  Array will have either 3 ro 4 cards
		Returns:
			Success or Failure as True/False
	"""
    # Move all Jokers to the end of the sequence
    while sequence[0].isjoker:
        sequence.append(sequence.pop(0))

    # Compare Cards in sequence with 0th Card, except for Jokers.
    for card in sequence:
        if card.is_joker():
            continue
        if card.rank != sequence[0].rank:
            return False

    return True
