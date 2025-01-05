def count_impossible_prices(N):
    for _ in range(N):
        A, B, T = map(float, input().split())
        impossible_count = 0
        
        # Iterate over all prices in the interval [A, B]
        for price in range(int(A * 100), int(B * 100) + 1):
            # Convert price back to float and calculate the after-tax price
            pre_tax_price = price / 100
            ATP = round(pre_tax_price * (1 + T / 100), 2)
            
            # Check if the calculated ATP is different from the original price
            if round(ATP * 100) != price:
                impossible_count += 1
        
        print(impossible_count)

# Read the number of test cases
N = int(input())
count_impossible_prices(N)
# Generator time: 10.3817 seconds