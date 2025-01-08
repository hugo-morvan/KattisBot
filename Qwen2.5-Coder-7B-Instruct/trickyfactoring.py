def count_possible_b(a, c):
    factors_a = set()
    factors_c = set()
    
    # Find all divisors of a
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            factors_a.add(i)
            factors_a.add(a // i)
    
    # Find all divisors of c
    for i in range(1, int(c**0.5) + 1):
        if c % i == 0:
            factors_c.add(i)
            factors_c.add(c // i)
    
    count = 0
    
    # Check all combinations of (d, e) and (f, g)
    for d in factors_a:
        for f in factors_a:
            for e in factors_c:
                for g in factors_c:
                    if d * f == a and e * g == c:
                        count += 1
    
    return count

# Input
a, c = map(int, input().split())

# Output
print(count_possible_b(a, c))
# Generator time: 7.7559 seconds