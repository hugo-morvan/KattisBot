import sys

def solve_case(s):
    n = len(s)
    total_points = sum(s)
    
    # Calculate the minimum audience vote fraction required for each contestant to avoid elimination
    min_votes = [1.0] * n
    
    # Sort contestants by their judge-assigned points in descending order
    sorted_indices = sorted(range(n), key=lambda i: s[i], reverse=True)
    
    # Calculate the minimum votes required
    remaining_votes = 1.0
    for i in range(1, n):
        min_votes[sorted_indices[i]] = (s[sorted_indices[i]] - s[sorted_indices[i-1]]) / total_points
    
    return min_votes

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        s = list(map(int, data[index:index + N]))
        index += N
        
        min_votes = solve_case(s)
        results.append(min_votes)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}:", end=" ")
        for m in result:
            print(f"{m:.6f}", end=" ")
        print()

if __name__ == "__main__":
    main()
# Generator time: 40.0580 seconds