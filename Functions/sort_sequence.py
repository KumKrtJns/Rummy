from constants import RANK_VALUE, SUIT_VALUE


def sort_sequence(sequence):
    """ Sort the Cards in the sequence in the incresing order of RANK values
		Args:
			sequence: array of Card objects
		Returns:
			sorted sequence.
	"""
    sequence = sorted(sequence, key=lambda Card: SUIT_VALUE[Card.suit])
    is_sort_complete = False

    while not is_sort_complete:
        is_sort_complete = True
        for i in range(len(sequence) - 1):
            if RANK_VALUE[sequence[i].rank] > RANK_VALUE[sequence[i + 1].rank] and sequence[i].suit == sequence[i + 1].suit:
                a = sequence[i + 1]
                sequence[i + 1] = sequence[i]
                sequence[i] = a
                is_sort_complete = False
    return sequence
