import sys
import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    Q = int(data[1])

    difficulties = list(map(int, data[2:2+N]))
    difficulties.sort()
    
    queries = []
    index = 2 + N
    for _ in range(Q):
        T = int(data[index])
        D = int(data[index+1])
        queries.append((T, D))
        index += 2

    for T, D in queries:
        if T == 1:
            # Find the easiest problem strictly harder than D
            pos = bisect.bisect_left(difficulties, D + 1)
            if pos < N:
                print(difficulties[pos])
                difficulties.pop(pos)
            else:
                print(-1)
        elif T == 2:
            # Find the hardest problem not harder than D
            pos = bisect.bisect_right(difficulties, D) - 1
            if pos >= 0:
                print(difficulties[pos])
                difficulties.pop(pos)
            else:
                print(-1)

if __name__ == "__main__":
    main()
# Generator time: 35.0592 seconds