from constants import RANK_VALUE
from Functions import sort_sequence
from Functions import push_joker_toend


def is_valid_run_joker(sequence):
    """ Check if the sequence with Jokers is a valid run.
		Args:
			sequence: an array of Card objects.  Array will have either 3 ro 4 cards
		Returns:
			Success or Failure as True/False
	"""

    RANK_VALUE["A"] = 1  # resetting value of A (may have been set to 14 in previous run)

    # Order the Cards in the sequence
    sequence = sort_sequence(sequence)

    # Push all Jokers to the end and count the number of Jokers
    push_joker_toend(sequence)
    joker_count = 0
    for card in sequence:
        if card.is_joker():
            joker_count += 1

    # Make sure the Suit Match except for Jokers.
    for card in sequence:
        if card.is_joker():
            continue
        if card.suit != sequence[0].suit:
            return False

    # This is to cover for K, Q and A run with Jokers
    if sequence[0].rank == "A":
        if sequence[1].rank == "Q" or sequence[1].rank == "J" or sequence[1].rank == "K":
            RANK_VALUE[sequence[0].rank] = 14
            sequence = sort_sequence(sequence)
            push_joker_toend(sequence)

    rank_inc = 1
    for i in range(1, len(sequence)):
        if sequence[i].is_joker():
            continue
        # Compare RANK values with accommodating for Jokers.
        while RANK_VALUE[sequence[i].rank] != RANK_VALUE[sequence[i - 1].rank] + rank_inc:
            # Use Joker Count for missing Cards in the run
            if joker_count > 0:
                rank_inc += 1
                joker_count -= 1
                continue
            else:
                # if No more Jokers left, then revert to regular comparison
                if RANK_VALUE[sequence[i].rank] != RANK_VALUE[sequence[i - 1].rank] + 1:
                    return False
                else:
                    break
    return True
