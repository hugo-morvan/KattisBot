import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    hearings = []
    
    for i in range(n):
        s = int(data[2 * i + 1])
        a = int(data[2 * i + 2])
        b = int(data[2 * i + 3])
        hearings.append((s, a, b))
    
    def expected_attendees(hearings):
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(i, end_time):
            if i == n:
                return 0
            s, a, b = hearings[i]
            if s >= end_time:
                # Attend this hearing
                min_length = max(s, end_time) - s + a
                max_length = max(s, end_time) - s + b
                expected_next_attendees_min = dp(i + 1, max(s, end_time) + min_length)
                expected_next_attendees_max = dp(i + 1, max(s, end_time) + max_length)
                return 1 + (expected_next_attendees_min + expected_next_attendees_max) / 2
            else:
                # Skip this hearing
                return dp(i + 1, end_time)
        
        return dp(0, 0)
    
    result = expected_attendees(tuple(hearings))
    print(f"{result:.3f}")

if __name__ == "__main__":
    main()
# Generator time: 44.4722 seconds