import sys

def calculate_min_percentage(N, scores):
    total_judge_points = sum(scores)
    min_scores = [float('inf')] * N
    
    # Iterate over each contestant's score
    for i, score in enumerate(scores):
        min_score = float('inf')
        
        # Calculate the minimum score needed for this contestant to avoid elimination
        for j in range(N):
            if i != j:
                # Calculate the remaining score needed to beat the current minimum score
                remaining_needed = min_scores[j] - score
                # Calculate the minimum fraction of audience votes needed
                if remaining_needed > 0:
                    min_fraction = remaining_needed / (total_judge_points - scores[i])
                    min_score = min(min_score, min_fraction)
        
        # Update the minimum score for this contestant
        min_scores[i] = min_score
    
    # Convert the minimum scores to percentages
    min_percentages = [min_score * 100 for min_score in min_scores]
    
    return min_percentages

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    start = 1
    
    for _ in range(T):
        N = int(data[start])
        scores = list(map(int, data[start + 1:start + N + 1]))
        min_percentages = calculate_min_percentage(N, scores)
        print(f"Case #{start // 2}: {' '.join(f'{p:.5f}' for p in min_percentages)}")
        start += N + 1

if __name__ == "__main__":
    main()
# Generator time: 17.5220 seconds