def count_impossible_prices(A, B, T):
    ATP = lambda x: round(x * (1 + T / 100), 2)
    impossible_count = 0
    
    for price in range(int(100 * A), int(100 * B) + 1):
        pre_tax_price = price / 100
        after_tax_price = ATP(pre_tax_price)
        if not (pre_tax_price <= A and pre_tax_price >= max(A, after_tax_price - 0.005)):
            impossible_count += 1
    
    return impossible_count

def main():
    N = int(input())
    results = []
    
    for _ in range(N):
        A, B, T = map(float, input().split())
        results.append(count_impossible_prices(A, B, T))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 7.4861 seconds