def count_cp_sequences(S):
    if S == 1:
        return 1
    count = 0
    for i in range(2, int(S**0.5) + 1):
        if S % i == 0:
            count += count_cp_sequences(i)
            if i != S // i:
                count += count_cp_sequences(S // i)
    return count + 1

def main():
    t = int(input())
    results = []
    for _ in range(t):
        S = int(input())
        results.append(count_cp_sequences(S))
    print(' '.join(map(str, results)))

if __name__ == "__main__":
    main()
# Generator time: 6.1366 seconds