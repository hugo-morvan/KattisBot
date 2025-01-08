import math

def min_processing_time(s, t, blades):
    def time_to_process(start_size, max_size, halving_time):
        if start_size > max_size:
            return float('inf')
        return (math.log2(start_size / max_size) * halving_time)

    min_time = float('inf')
    for m, h in blades:
        processing_time = time_to_process(s, m, h)
        if processing_time == float('inf'):
            continue
        pieces_after_processing = s / (2 ** (processing_time / h))
        additional_time = 0
        while pieces_after_processing > t:
            additional_time += h
            pieces_after_processing /= 2
        min_time = min(min_time, processing_time + additional_time)

    return min_time if min_time != float('inf') else -1

# Input reading
s, t, n = map(int, input().split())
blades = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_processing_time(s, t, blades))
# Generator time: 30.2806 seconds