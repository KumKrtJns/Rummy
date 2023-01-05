from Functions import sort_sequence


def push_joker_toend(sequence):
    """ Push the Joker to the end of the sequence.
		Args:
			sequence: sequence of Card Objects.
		Returns:
			no return
	"""
    sequence = sort_sequence(sequence)
    joker_list = []
    for card in sequence:
        if card.is_joker():
            sequence.remove(card)
            joker_list.append(card)
    sequence += joker_list
    return sequence
