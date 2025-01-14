def prank(n, pairs):
	return sorted([pair for pair in pairs if not all(s in pairs for s in [pair[0], pair[1]] )])[0]
# Generator time: 3.7747 seconds