def get_object(arr, str_card):
    """ Get Card Object using its User Input string representation
	Args:
		arr: array of Card objects
		str_card: Card descriptor as described by user input, that is a 2 character
			string of Rank and Suit of the Card.  For example, KH for King of Hearts.
	Returns:
		object pointer corresponding to string, from the arr
	"""
    # Make sure the str_card has only a RANK letter and SUIT letter
    # for example KH for King of Hearts.
    if len(str_card) != 2:
        return None

    for item in arr:
        if item.rank == str_card[0] and item.suit[0] == str_card[1]:
            return item

    return None
