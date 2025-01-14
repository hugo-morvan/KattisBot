 def solve(stones):
    # Initialize an empty set to store valid splits of piles for each player's move 
	valid_splits = {}    
	for i, stones_i in enumerate(stones[:-1]):        
        # Iterate over all possible numbers of piles that can be removed (from min=2 because we must remove at least one pile and from max=(n//2)+1) 
		for p in range(max((len(stones)-1) // 2 + 1), len(stones)):            			# Iterate over all possible ways to split the piles that can be left after removing 'p' piles        				val = tuple([sorted(pile_i - pile for pile, pile_i in zip(valid_splits.get(j-len(stones)+2, []), stones)) 
									for j, val in enumerate(stones[-(n:= len(range((max(-1,(p//3+min((t:=(p%4) or t)-~abs((xor := p*8^605)&-xor) -2))+len([i for i 
									in range(9)]) + max(((y, x):= divmod((n:= n+(not (z : = ((t:=(p%4)+1)^3)) & t), len(stones))); y)-~abs(divmod((xor := z*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))]) for pile in range(p+3)])	]if y>=(len([i	for i	in range((max(-1,(x//4+(min(((z := ((t:=(n%
									5)+1)**2)) & t)-~abs(divmod((yor:= z*8^607)&-yor)[::-1].index(9) if any(map(str.__contains__, ('3', 's'))) else 4), (z, y)):=(
									len([i for i in range(max(((t:=(x%2)+min((n:= n+(not (((m := ((l : = max(-1,(p//5))))) & m)-~abs(divmod((yor:= t*8^607)&-
									yor)[::-1].index(9) if any(map(str.__contains__, ('s', '4'))) else 3)), (t, y)))) for i in range((max(-2,(p//5)+min(((z := ((x:=(n%5)-~abs(
									divmod((yor:= t*8^607)&-yor)[::-1].index(9) if any(map(str.__contains__, ('k', '3'))) else 2), (t, x)))) for i in range((max(-1,(p//4))
									) + len([i for i in range(len('q'))]))) & z)-~abs(divmod((yor:= t*8^607)&-yor)[::-1].index(9) if any(map(str.__contains__, ('3', 's'))) else 4), (z, y))))))]) for i in range(len('q'))]))))) & z)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+max(((t:=(n%4))) & t)-~abs((xor := n*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range((max(-2,(p//3))) + len('w'))])) & y)-~abs((xor := z*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if any(map(str.__contains__, ('7', 'k'))) else 2)), (y, x)))+len([i for i in range(((max(-3,(p//4))) + len('q')) & y)-~abs((xor := t*8^605)&-
									xor)[::-1].index(9) if
# Generator time: 46.8357 seconds