from constants import RANK_VALUE
from Functions import sort_sequence


def is_valid_run(sequence):
    """ Check if the sequence is a valid run.
		Args:
			sequence: an array of Card objects.  Array will have either 3 ro 4 cards
		Returns:
			Success or Failure as True/False
	"""
    RANK_VALUE["A"] = 1  # resetting value of A (may have been set to 14 in previous run)

    # Order the Cards in the sequence
    sequence = sort_sequence(sequence)

    # Check to see if all Cards in the sequence have the same SUIT
    for card in sequence:
        if card.suit != sequence[0].suit:
            return False

    # this is to sort a sequence that has J, Q and A
    if sequence[0].rank == "A":
        if sequence[1].rank == "Q" or sequence[1].rank == "J" or sequence[1].rank == "K":
            RANK_VALUE[sequence[0].rank] = 14
            sequence = sort_sequence(sequence)

    # Rank Comparison
    for i in range(1, len(sequence)):
        if RANK_VALUE[sequence[i].rank] != RANK_VALUE[sequence[i - 1].rank] + 1:
            return False

    return True
