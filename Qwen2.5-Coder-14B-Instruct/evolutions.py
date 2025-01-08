def count_cp_sequences(S):
    def is_power_of_integer(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            x = n
            while x % i == 0:
                x //= i
            if x == 1:
                return True
        return False

    count = 0
    for k in range(1, S):
        if is_power_of_integer(S // k):
            count += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    index = 1
    
    for _ in range(t):
        S = int(data[index])
        results.append(count_cp_sequences(S))
        index += 1
    
    print(*results)

if __name__ == "__main__":
    main()
# Generator time: 27.9251 seconds