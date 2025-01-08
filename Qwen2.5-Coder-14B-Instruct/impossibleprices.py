def count_impossible_prices(N):
    import math
    
    def is_possible_price(price, T):
        pre_tax = price / (1 + T / 100)
        rounded = round(pre_tax * 100) / 100
        return abs(rounded - price) < 0.005
    
    results = []
    
    for _ in range(N):
        A, B, T = map(float, input().split())
        count = 0
        
        # Iterate over possible after-tax prices
        price = math.ceil(A * 100) / 100
        while price <= B:
            if not is_possible_price(price, T):
                count += 1
            price += 0.01
    
        results.append(count)
    
    for result in results:
        print(result)

# Read the number of test cases
N = int(input())
count_impossible_prices(N)
# Generator time: 27.6594 seconds