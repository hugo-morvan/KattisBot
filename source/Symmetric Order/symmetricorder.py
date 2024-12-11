def process_input():
    while True:
        n = int(input())
        if n == 0:
            break
        
        names = []
        for _ in range(n):
            names.append(input())
        
        # Sort names by length
        names.sort(key=len)
        
        # Create pairs of names from the sorted list
        pairs = []
        for i in range(0, len(names), 2):
            pairs.append((names[i], names[i + 1]))
        
        # Print the result for the current set
        print(f"SET {len(pairs) + 1}")
        for pair in pairs:
            print(pair[0], pair[1])

process_input()