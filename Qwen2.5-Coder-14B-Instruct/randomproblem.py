def find_triple_correlation(p, digits):
    min_occurrences = (p + 39) // 40 + 1
    
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for n in range(1, p - 1):
                    for m in range(1, p - n):
                        occurrences = 0
                        valid = True
                        
                        for i in range(p - n - m):
                            if digits[i] == a and digits[i + n] == b and digits[i + n + m] == c:
                                occurrences += 1
                            elif digits[i] == b and digits[i + m] == c and (i < n or i + m + n >= p):
                                valid = False
                                break
                            elif digits[i] == a and digits[i + n + m] == c and (i < n or i + n + m + n >= p):
                                valid = False
                                break
                        
                        if valid and occurrences >= min_occurrences:
                            return f"{a}({n}){b}({m}){c}"
    
    return "random sequence"

# Read input
p = int(input().strip())
digits = []

while True:
    line = input().strip()
    if not line:
        break
    digits.extend(map(int, line.split()))

# Find and print the result
print(find_triple_correlation(p, digits))
# Generator time: 42.6422 seconds