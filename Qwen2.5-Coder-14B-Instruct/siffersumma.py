def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def next_same_digit_sum(N):
    target_sum = digit_sum(N)
    candidate = N + 1
    
    while True:
        if digit_sum(candidate) == target_sum:
            return candidate
        candidate += 1

N = int(input())
result = next_same_digit_sum(N)
print(result)
# Generator time: 12.1556 seconds