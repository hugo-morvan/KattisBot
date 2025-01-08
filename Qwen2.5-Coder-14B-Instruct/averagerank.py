import sys
from collections import defaultdict

def calculate_average_ranks(n, w, points_per_week):
    scores = [0] * n
    ranks = [0] * n
    
    for week_points in points_per_week:
        for competitor in week_points:
            scores[competitor - 1] += 1
    
    total_ranks = defaultdict(float)
    
    for week in range(w):
        current_scores = scores[:]
        current_scores.sort(reverse=True)
        
        rank = 1
        previous_score = float('inf')
        for i, score in enumerate(current_scores):
            if score != previous_score:
                rank = i + 1
            total_ranks[current_scores.index(score) + 1] += rank
            previous_score = score
    
    average_ranks = [total_ranks[i + 1] / w for i in range(n)]
    
    for avg_rank in average_ranks:
        print(f"{avg_rank:.6f}")

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    w = int(data[index + 1])
    index += 2
    
    points_per_week = []
    for _ in range(w):
        k = int(data[index])
        index += 1
        week_points = [int(data[index + i]) for i in range(k)]
        index += k
        points_per_week.append(week_points)
    
    calculate_average_ranks(n, w, points_per_week)

if __name__ == "__main__":
    main()
# Generator time: 43.5828 seconds