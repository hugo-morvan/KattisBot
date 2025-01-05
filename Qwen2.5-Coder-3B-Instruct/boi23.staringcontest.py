import sys

def main():
    n = int(input())
    queries = []
    
    # Generate all possible pairs of athletes
    for i in range(n):
        for j in range(i + 1, n):
            queries.append((i, j))
    
    # Perform queries and store results
    results = {}
    for i, j in queries:
        result = int(input("? {} {}".format(i + 1, j + 1)))
        results[(i, j)] = result
    
    # Calculate the estimated strengths
    estimates = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) in results:
                estimates[i] = max(estimates[i], results[(i, j)])
                estimates[j] = max(estimates[j], results[(i, j)])
    
    # Output the estimates
    print("! ", end="")
    for b in estimates:
        print(b, end=" ")
    print()

if __name__ == "__main__":
    main()
# Generator time: 12.8114 seconds