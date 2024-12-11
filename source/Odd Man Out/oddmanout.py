def find_alone_guest():
    T = int(input())
    for t in range(1, T + 1):
        G = int(input())
        codes = list(map(int, input().split()))
        
        # Count the occurrences of each code
        from collections import Counter
        code_counts = Counter(codes)
        
        # Find the code that appears once
        for code, count in code_counts.items():
            if count == 1:
                print(f"Case #{t}: {code}")
                break

find_alone_guest()