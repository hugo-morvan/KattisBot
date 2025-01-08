from typing import List

def expected_hearings(n: int, hearings: List[List[int]]) -> float:
    dp = [0] * n
    for i in range(n-1, -1, -1):
        s, a, b = hearings[i]
        min_end = s + a
        max_end = s + b
        if i == n-1:
            dp[i] = 1
        else:
            total_prob = 0
            for end in range(min_end, max_end+1):
                next_start = end
                count = 0
                prob = 1.0
                while next_start < hearings[i+1][0]:
                    count += 1
                    next_end = s + a
                    if next_start + a <= hearings[i+1][0]:
                        next_end += (hearings[i+1][0] - next_start)
                        prob *= (next_end - next_start) / (b - a + 1)
                    next_start = next_end
                total_prob += prob * count
            dp[i] = 1 + total_prob
    
    return sum(dp) / n

def main():
    n = int(input())
    hearings = [list(map(int, input().split())) for _ in range(n)]
    result = expected_hearings(n, hearings)
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()
# Generator time: 10.2525 seconds