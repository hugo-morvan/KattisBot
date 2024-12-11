import sys

def main():
    # Read input
    n, k = map(int, input().split())
    ratings = list(map(int, input().split()))
    
    # Calculate current sum and count
    current_sum = sum(ratings)
    current_count = len(ratings)
    
    # Calculate minimum and maximum possible overall rating
    min_rating = (current_sum - 3 * (n - current_count)) / (n - current_count)
    max_rating = (current_sum + 3 * (n - current_count)) / (n - current_count)
    
    # Print the result
    print(f"{min_rating:.4f} {max_rating:.4f}")

if __name__ == "__main__":
    main()