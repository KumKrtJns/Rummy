def print_cards(arr):
    """ Print Cards in a single line
		Args:
			arr: array of Card Objects
		Returns:
			a displayable string representation of the Cards in the arr
	"""
    s = ""
    for card in arr:
        s = s + " " + str(card)
    return s