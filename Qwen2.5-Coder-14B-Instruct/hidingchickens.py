import itertools
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def min_distance_to_hide_chickens(roost, hiding_spots):
    n = len(hiding_spots)
    all_pairs = list(itertools.combinations(range(n), 2))
    dp = {(frozenset(), i): distance(roost, hiding_spots[i]) for i in range(n)}
    
    for k in range(2, n + 1):
        for subset in itertools.combinations(range(n), k):
            subset_set = frozenset(subset)
            for j in range(k):
                if j not in subset:
                    continue
                remaining_subset = subset_set - {j}
                dp[subset_set, j] = min(dp.get((remaining_subset, i), float('inf')) + distance(hiding_spots[i], hiding_spots[j])
                                        for i in remaining_subset)
    
    return min(dp[(frozenset(range(n)), i)] for i in range(n))

def main():
    x, y = map(float, input().split())
    roost = (x, y)
    n = int(input())
    hiding_spots = [tuple(map(float, input().split())) for _ in range(n)]
    
    result = min_distance_to_hide_chickens(roost, hiding_spots)
    print(f"{result:.6f}")

if __name__ == "__main__":
    main()
# Generator time: 42.6332 seconds