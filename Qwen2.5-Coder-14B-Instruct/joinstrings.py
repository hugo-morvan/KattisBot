import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    strings = data[1:1 + N]
    operations = list(zip(map(int, data[N + 1::2]), map(int, data[N + 2::2])))
    
    for a, b in operations:
        strings[a - 1] += strings[b - 1]
        strings[b - 1] = ""
    
    for s in strings:
        if s:
            print(s)
            return

if __name__ == "__main__":
    main()
# Generator time: 21.2469 seconds