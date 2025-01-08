def calculate_min_percentage(s):
    N = len(s)
    total_judges_points = sum(s)
    sorted_scores = sorted((s[i], i) for i in range(N))
    
    min_percentages = []
    for i, (judge_score, index) in enumerate(sorted_scores):
        remaining_points = total_judges_points - judge_score
        if i == N - 1:
            min_percentage = 0.0
        else:
            remaining_contestants = N - i - 1
            required_audience_points = remaining_points * (i + 2) / (remaining_contestants + 1)
            min_percentage = required_audience_points / total_judges_points
        
        min_percentages.append(min_percentage)
    
    return min_percentages

def main():
    T = int(input())
    results = []
    
    for t in range(1, T + 1):
        N, *s = map(int, input().split())
        result = calculate_min_percentage(s)
        results.append(f"Case #{t}: {' '.join(map(lambda x: f'{x:.6f}', result))}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 8.8180 seconds