def find_resulting_color(rules, tokens):
    while len(tokens) > 1:
        max_certainty = -1
        best_move = None
        
        for i in range(len(tokens) - 1):
            s1, s2 = tokens[i], tokens[i + 1]
            if (s1, s2) in rules or (s2, s1) in rules:
                c1, c2 = sum(c for _, c in tokens[i][1]), sum(c for _, c in tokens[i + 1][1])
                certainty = c1 * c2
                if certainty > max_certainty:
                    max_certainty = certainty
                    best_move = (i, s1, s2)
        
        if best_move is None:
            return "GAMEOVER"
        
        i, s1, s2 = best_move
        result_color = rules.get((s1, s2), rules.get((s2, s1)))
        tokens[i:i + 2] = [(result_color, max_certainty)]
    
    return tokens[0][0]

def main():
    R = int(input().strip())
    rules = {}
    
    for _ in range(R):
        s1, s2, s3 = input().strip().split()
        rules[(s1, s2)] = s3
    
    T = int(input().strip())
    
    results = []
    
    for _ in range(T):
        C = int(input().strip())
        tokens = []
        
        for _ in range(C):
            line = input().strip()
            if line == "END":
                break
            color, certainty = line.split()
            tokens.append((color, [float(certainty)]))
        
        result = find_resulting_color(rules, tokens)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 12.5394 seconds