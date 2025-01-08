def smallest_integer_with_same_digit_sum(N):
    def digit_sum(n):
        return sum(int(digit) for digit in str(n))
    
    target_sum = digit_sum(N)
    current = N + 1
    
    while True:
        if digit_sum(current) == target_sum:
            return current
        current += 1

# Example usage:
N = int(input())
print(smallest_integer_with_same_digit_sum(N))
# Generator time: 4.3986 seconds