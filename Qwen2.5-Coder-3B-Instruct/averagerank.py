from collections import defaultdict
import math

def calculate_average_rank(n, w, events):
    # Initialize the ranks dictionary with each competitor having a rank of n+1
    ranks = {i: n + 1 for i in range(1, n + 1)}
    
    # Initialize the score dictionary with each competitor having a score of 0
    scores = {i: 0 for i in range(1, n + 1)}
    
    # Process each event
    for week, participants in events:
        for participant in participants:
            scores[participant] += 1
    
    # Sort the scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Assign ranks based on sorted scores
    rank = 1
    for score, participant in sorted_scores:
        ranks[participant] = rank
        rank += 1
    
    # Calculate the average rank for each competitor
    average_ranks = [ranks[i] / w for i in range(1, n + 1)]
    
    # Print the average ranks
    for rank in average_ranks:
        print(f"{rank:.6f}")

# Read input
n, w = map(int, input().split())
events = []

for _ in range(w):
    k = int(input())
    participants = list(map(int, input().split()))
    events.append((k, participants))

# Calculate and print the average ranks
calculate_average_rank(n, w, events)
# Generator time: 13.9386 seconds