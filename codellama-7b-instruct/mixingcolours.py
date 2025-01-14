def solve(R, rules, T, tests):
    # build a dict of all rules
    rule_dict = {(r[0], r[1]): r[2] for r in rules}

    # build a set of allowed colors
    allowed = set()
    for r in rules:
        if r[0] not in allowed:
            allowed.add(r[0])
        if r[2] not in allowed:
            allowed.add(r[2])
    
    # build a dict of certainties for each token
    token_dict = {}
    for t in tests:
        for tt in t:
            if tt[0] not in token_dict:
                token_dict[tt[0]] = 1.0 * tt[1]
            else:
                token_dict[tt[0]] += 1.0 * tt[1]
    
    # compute the likely color
    for t in tests:
        if len(t) == 1:
            yield token_dict[t[0][0]]
            continue
        
        for i in range(len(t) - 1):
            # find a combination of two adjacent tokens that can be combined
            while t[i][0] != t[i+1][0]:
                i += 1
            if t[i][0] == t[i-1][0]:
                yield rule_dict[(t[i-1][0], t[i][0])]
                return
    
        # check the last token with all colors allowed
        for c in allowed:
            if (c, t[-1][0]) in rule_dict:
                yield rule_dict[(c, t[-1][0])]
                return
        
    # no possible combination exists
    yield "GAMEOVER"
# Generator time: 31.1225 seconds